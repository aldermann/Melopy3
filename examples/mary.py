import os

from melopy import Melopy


def main():
    m = Melopy('mary')
    d = os.path.dirname(__file__)
    if len(d):
        m.parsefile(d + '/scores/mary.mlp')
    else:
        m.parsefile('scores/mary.mlp')
    m.render()
    m.play()


if __name__ == '__main__':
    main()
