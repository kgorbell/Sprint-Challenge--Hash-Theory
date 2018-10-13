def get_indices_of_item_weights(weights, limit):
  # tuple = ()
  # dict = zip(weights, range(len(weights))


  dict = {}
  for i in range(len(weights)):
    weight = weights[i]
    if (limit - weight) in dict:
      return (i, dict[limit - weight])
    else:
      dict[weight] = i
  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 