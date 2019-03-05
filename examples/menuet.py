import os

from melopy import Melopy


def main():
    m = Melopy('menuet')
    d = os.path.dirname(__file__)
    if len(d):
        m.parsefile(d + '/scores/menuet.mlp')
    else:
        m.parsefile('scores/menuet.mlp')
    m.render()
    m.play()


if __name__ == '__main__':
    main()
