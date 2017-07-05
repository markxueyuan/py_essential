class SecretString:
    '''A not-at-all secure way to store a secret string.'''
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string # name mangling
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''

def main():
    secretstring = SecretString("ACME: Top Secret", "antwerp")
    print(secretstring.decrypt("antwerp"))
    try:
        secretstring.__plain_string
    except AttributeError as e:
        print(e)
    print(secretstring._SecretString__plain_string) # hack name mangling


if __name__ == "__main__":
    main()