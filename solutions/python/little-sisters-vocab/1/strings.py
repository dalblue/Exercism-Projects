"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    Parameters:
        word (str): The root word.
    Returns:
        str: Root word prepended with 'un'.
    """
    preadd='un'
    postadd=preadd+word
    return postadd


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.
    Returns:
        str: Prefix followed by vocabulary words with prefix applied.
    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.
    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.
    """
    preadd=vocab_words[0]
    postlist=f"{vocab_words[0]} :: "
    for word in vocab_words[1:]:
        if word!=vocab_words[-1]:
            postlist+=preadd+word+' :: '
        if word==vocab_words[-1]:
            postlist+=preadd+word
    return postlist


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
    Parameters:
        word (str): Word to remove suffix from.
    Returns:
        str: Word with suffix removed & spelling adjusted.
    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'
        >>> remove_suffix_ness('sadness')
        'sad'
    """
    newword=''
    if word[-5]!='i':
        newword+=word[0:len(word)-4]
    if word[-5]=='i':
        newword+=word[0:len(word)-5]+'y'
    return newword


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.
    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.
    Returns:
        str: The extracted adjective in verb form.
    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'
        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'
    """
    punctuation=[".",",","'","\"", "?","!"]
    newword=""
    words=sentence.split(" ")
    if words[index][-1] in punctuation:
        newword=words[index][0:len(words[index])-1]+"en"
    if words[index][-1] not in punctuation:
        newword=words[index]+"en"
    return newword