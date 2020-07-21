import scribunto


def test_search_dependencies() -> None:
    text = '''
local mHatnote = require('Module:Hatnote')
local mHatList = require('Module:Hatnote list')
local libraryUtil = require('libraryUtil')
local checkType = libraryUtil.checkType
local p = {}
'''

    expected = [
        'Hatnote',
        'Hatnote list',
    ]
    actual = scribunto.search_dependencies(text)

    assert actual.sort() == expected.sort()

    # with prefix

    text = '''
local mHatnote = require('Module:Hatnote')
local mHatList = require('Module:Hatnote list')
'''

    expected = [
        '@en/Hatnote',
        '@en/Hatnote list',
    ]
    actual = scribunto.search_dependencies(text, prefix='en')

    assert actual.sort() == expected.sort()


def test_rewrite_requires() -> None:
    text = '''
local mHatnote = require('Module:Hatnote')
local mHatList = require('Module:Hatnote list')
local libraryUtil = require('libraryUtil')
local checkType = libraryUtil.checkType
local p = {}
'''

    expected = '''
local mHatnote = require('Module:@en/Hatnote')
local mHatList = require('Module:@en/Hatnote list')
local libraryUtil = require('libraryUtil')
local checkType = libraryUtil.checkType
local p = {}
'''
    actual = scribunto.rewrite_requires(text, 'en')

    assert actual == expected

    text = "require('Module:Foo/bar')"
    expected = "require('Module:@en/Foo-bar')"
    actual = scribunto.rewrite_requires(text, 'en')

    assert actual == expected