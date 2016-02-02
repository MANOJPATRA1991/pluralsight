#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """
    Provides an empty phonebook.
    """
    phonebook = Phonebook(tmpdir)
    return phonebook

# @pytest.skip("WIP")
# above skips ALL the tests in the file


def test_add_and_lookup_entry(phonebook):
    # pytest.skip("WIP")
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob"), "Bob not found"


def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    # assert "Ali" in phonebook.names()
    assert "Alice" in phonebook.names()
    assert set(phonebook.names()) == {"Alice", "Bob"}
    assert "12345" in phonebook.numbers()


def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")
