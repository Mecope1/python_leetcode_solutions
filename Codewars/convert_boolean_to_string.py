def bool_to_word(boolean):
    # This allows for logical short circuiting. This is also chainable!
    return 'Yes' if boolean else 'No'

    # This does NOT allow for logical short circuiting
    # return ('No', 'Yes')[boolean]