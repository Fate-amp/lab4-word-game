import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import (
    display_word_state,
    initialize_game,
    is_lost,
    is_won,
    update_game_state,
    validate_guess,
)


@pytest.mark.parametrize(
    ("guess", "starting_guesses", "expected_guesses", "starting_lives", "expected_lives"),
    [
        pytest.param("h", [], ["h"], 5, 5, id="new-correct-guess"),
        pytest.param("H", [], ["h"], 5, 5, id="correct-guess-normalized"),
        pytest.param("h", ["h"], ["h"], 5, 5, id="repeated-correct-guess-same-case"),
        pytest.param("H", ["h"], ["h"], 5, 5, id="repeated-correct-guess-different-case"),
    ],
)
def test_correct_and_repeated_guesses_update_state_as_expected(
    guess: str,
    starting_guesses: list[str],
    expected_guesses: list[str],
    starting_lives: int,
    expected_lives: int,
) -> None:
    guessed, lives = update_game_state("hello", starting_guesses, guess, starting_lives)

    assert guessed == expected_guesses, (
        f"Guess {guess!r} should produce guessed_letters={expected_guesses}, but got {guessed}."
    )
    assert lives == expected_lives, (
        f"Guess {guess!r} should leave lives at {expected_lives}, but got {lives}."
    )


def test_wrong_guess_decrements_life() -> None:
    guessed, lives = update_game_state("hello", [], "z", 5)

    assert guessed == [], "A wrong guess should not be added to guessed_letters."
    assert lives == 4, "A wrong guess should cost exactly one life."


@pytest.mark.parametrize(
    "guess",
    [
        pytest.param("", id="empty-string"),
        pytest.param("!", id="special-character"),
        pytest.param("he", id="multiple-letters"),
        pytest.param(" ", id="space"),
    ],
)
def test_invalid_guess_does_not_change_state(guess: str) -> None:
    guessed, lives = update_game_state("hello", [], guess, 5)

    assert guessed == [], (
        f"Invalid guess {guess!r} should not add anything to guessed_letters, but got {guessed}."
    )
    assert lives == 5, f"Invalid guess {guess!r} should not change lives, but got {lives}."


def test_does_not_mutate_input_guessed_letters() -> None:
    original = ["h"]

    guessed, lives = update_game_state("hello", original, "e", 5)

    assert original == ["h"], "update_game_state should not mutate the caller's list."
    assert guessed == ["h", "e"]
    assert lives == 5


def test_initialize_game_sets_expected_starting_values() -> None:
    state = initialize_game("hello")

    assert state == {
        "guessed_letters": [],
        "lives": 5,
        "wrong_letters": [],
    }


def test_display_word_state_masks_unknown_letters() -> None:
    assert display_word_state("hello", ["h", "l"]) == "h_ll_"


def test_display_word_state_reveals_repeated_letters() -> None:
    assert display_word_state("letter", ["t", "e"]) == "_ette_"


def test_is_won_returns_true_when_all_letters_are_guessed() -> None:
    assert is_won("hello", ["h", "e", "l", "o"])


def test_is_won_returns_false_when_word_is_incomplete() -> None:
    assert not is_won("hello", ["h", "e", "l"])


def test_is_lost_returns_true_at_zero_lives() -> None:
    assert is_lost(0)


def test_is_lost_returns_false_when_lives_remain() -> None:
    assert not is_lost(1)


def test_validate_guess_accepts_single_letter() -> None:
    assert validate_guess("a")


@pytest.mark.parametrize(
    "guess",
    [
        pytest.param("", id="empty-string"),
        pytest.param("ab", id="multiple-letters"),
        pytest.param("!", id="special-character"),
        pytest.param(" ", id="space"),
    ],
)
def test_validate_guess_rejects_invalid_input(guess: str) -> None:
    assert not validate_guess(guess), f"Guess {guess!r} should be rejected as invalid."
