import bs
import bsGame

my_profile = 'Hi :) My name is Abbas Kassem, I am 16 years old, I am from Algeria\n\n-I like Python Programming, and editing BombSquad Game\n\n-I will be one of the bombsquad editors\n\n-Goodbye ;)'

def text():

    return bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'left',
            'vAlign': 'center',
            'vrDepth': 0,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': '-',
            'big': False,
            'position': (-600, 300),
            'color': (1,1,0)})


def test():

    n = bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 0,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': '12345678901234567890',
            'big': False,
            'position': (0, 27),
            'color': (1,1,0)})

    return n

def s():


    i = bs.newNode('image', attrs={
            'scale': (2000, 100),
            'texture': bs.getTexture('bar'),
            'position': (0, 27),
            'color': (1,1,0)})

    n = bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 0,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': 'BOOYAH',
            'big': True,
            'position': (0, 27),
            'color': (1,1,0)})

    c = bs.newNode('text', attrs={
            'hAttach': 'center',
            'vAttach': 'center',
            'hAlign': 'center',
            'vAlign': 'center',
            'vrDepth': 2,
            'scale': 1.0,
            'shadow': 1.0,
            'flatness': 1.0,
            'text': 'BOOYAH',
            'big': True,
            'position': (0, 27),
            'color': (1,1,0)})

    bs.animate(c, "scale", {0:1, 500:2})
    bs.animate(c, "opacity", {0:1, 500:0})
    bs.gameTimer(500, c.delete)
    return (n, i)

def add_txt(lifespan, node, txt):
    if not node.getNodeType() == 'text': return
    num = len(txt)
    added = list(txt)
    def a():
        node.text += added[0]
        added.pop(0)
    for i in range(num):
        bs.gameTimer((lifespan/num)*(i+1), a)

def del_txt(lifespan, node, cut):
    if not node.getNodeType() == 'text': return
    num = len(node.text)
    posi = round(num*cut[0])
    nega = round(-( num*(1.0-cut[1])))
    assert len(cut) == 2
    print(str(posi)+'  '+str(nega))
    def a():
        node.text = node.text[int(posi) if posi else None:int(nega) if nega else None]
    a()

def sort_key(item):
    return item[1]

def rk(players):
    ranked = sorted(players, key=sort_key, reverse=True)
    result = []
    for i, (players, score) in enumerate(ranked, start=1):
        result.append({
            'rank': i,
            'player': players,
            'score': score})
    return result

def players_rank():
    players = [('kassem', 150), ('khaled', 120), ('king cold', 220), ('Roshi', 100)]
    return rk(players)

class CutText(bsGame.Actor):
    def __init__(self, node):
        bs.Actor.__init__(self)
        self.node = node
        self.text_base = self.node.text
        self.num = len(node.text)
        self.last_cut = (0.0, 1.0)
    def del_txt(self, cut):
        if not self.node.getNodeType() == 'text': return
        self.posi = round(self.num*cut[0])
        self.nega = round(-(self.num*(1.0-cut[1])))
        assert len(cut) == 2
        self.last_cut = cut
        print(str(self.posi)+'  '+str(self.nega))
        self.node.text = self.text_base[int(self.posi) if self.posi else None:int(self.nega) if self.nega else None]

    def anim_cut(self, lifespan, cut):
        start = abs(self.last_cut[0] - cut[0])
        end = abs(self.last_cut[1] - cut[1])
        self.posi1 = round(self.num*start)
        self.nega1 = round((self.num*(1.0-start)))
        def del_posi():
            if cut[0] > self.last_cut[0]:
                self.del_txt((self.last_cut[0] + (start/self.posi1), self.last_cut[1]))
            else:
                self.del_txt((self.last_cut[0] - (start/self.posi1), self.last_cut[1]))

        def del_nega():
            if cut[1] > self.last_cut[1]:
                self.del_txt((self.last_cut[0], self.last_cut[1] + (end/self.nega1)))
            else:
                self.del_txt((self.last_cut[0], self.last_cut[1] - (end/self.nega1)))

        for i in range(int(self.posi1)):
            bs.gameTimer((lifespan/int(self.posi1))*(i+1), del_posi)

        for i in range(int(self.nega1)):
            bs.gameTimer((lifespan/int(self.nega1))*(i+1), del_nega)

class prr(bsGame.Actor):
  def __init__(self, node):
    if not node.getNodeType() == 'text': return
    self.lifespan = 0
    self.timer = None
    self.start = 0
    self.end = 0
    self.txt = ''
    self.node = node


    self.node.text = str(self.start)

  def add_int(self):
    if self.start < self.end:
      self.start += 1
      if self.txt:
          try: self.node.text = self.txt.format(num = str(self.start))
          except: self.node.text = self.txt.replace('{num}', str(self.start))
      else:
          self.node.text = str(self.start)
    else:
      self.start -= 1
      if self.txt:
          try: self.node.text = self.txt.format(num = str(self.start))
          except: self.node.text = self.txt.replace('{num}', str(self.start))

      else:
          self.node.text = str(self.start)

  def stop(self):
    self.timer = None

  def play(self, lifespan, start, end, txt):
    self.lifespan = lifespan
    self.start = start
    self.end = end
    self.txt = txt

    if txt:
      try: self.node.text = self.txt.format(num = str(self.start))
      except: self.node.text = self.txt.replace('{num}', str(self.start))

    else:
        self.node.text = str(self.start)

    abc = abs(self.start-self.end)
    self.timer = bs.Timer(self.lifespan/abc, self.add_int, repeat=True)
    bs.gameTimer(self.lifespan, self.stop)

class prr_adv(bsGame.Actor):
  def __init__(self, node):
    if not node.getNodeType() == 'text': return
    self.crono_dict = {}
    self.txt = ''
    self.node = node
    self.node.text = '0'

  def add_int(self, key):
    if self.crono_dict[key][1] < self.crono_dict[key][2]:
      self.crono_dict[key] = (self.crono_dict[key][0], self.crono_dict[key][1] + 1, self.crono_dict[key][2])
    if self.crono_dict[key][1] > self.crono_dict[key][2]:
      self.crono_dict[key] = (self.crono_dict[key][0], self.crono_dict[key][1] - 1, self.crono_dict[key][2])
    else:
      pass

    d = {a: self.crono_dict[a][1] for a in self.crono_dict}
    if self.txt:
      self.node.text = self.txt.format(**d)
    else:
      pass

  def play(self, txt, keys):
      self.txt = txt
      self.crono_dict = keys

      d = {a: self.crono_dict[a][1] for a in self.crono_dict}
      if self.txt:
        self.node.text = self.txt.format(**d)
      else:
        pass

      for i in self.crono_dict:
        abc = abs(self.crono_dict[i][1] - self.crono_dict[i][2])
        for r in range(abc):
          bs.gameTimer((self.crono_dict[i][0]/abc)*(r+1), bs.Call(self.add_int, i))
