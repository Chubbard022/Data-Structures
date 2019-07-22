class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.item = item
    add_item = self.storage.append(self.item)
    self.size += 1
    return add_item
  
  def dequeue(self):
    if self.size is 0:
      return None
    remove_item = self.storage.pop(0)
    self.size -= 1

    return remove_item
  def len(self):
    return self.size
