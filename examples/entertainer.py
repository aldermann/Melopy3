import os

from melopy import Melopy


def main():
    m = Melopy('entertainer')
    m.tempo = 140
    d = os.path.dirname(__file__)
    if len(d):
        m.parsefile(d + '/scores/entertainer.mlp')
    else:
        m.parsefile('scores/entertainer.mlp')
    m.render()
    m.play()


if __name__ == '__main__':
    main()
