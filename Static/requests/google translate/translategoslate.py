import goslate
text  = '''
『名探偵コナン100PLUS』発売記念緊急アンケート第2弾！
みんなが二人でおうちデートしたい『コナン』のキャラは？　理由も教えてね！

このツイートに返信するか、＃コナンおうちデート
をつけてツイートしてね！

結果は、春頃発売の『名探偵コナン100PLUS SDB』にて発表！
〆きりは3月3日24時！
'''
gs = goslate.Goslate()
print(gs.translate(text, 'en'))