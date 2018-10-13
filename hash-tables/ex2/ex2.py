def reconstruct_trip(tickets):
  tkt_dict = {}
  route = [''] * (len(tickets)-1)
  for tkt in tickets:
    tkt_dict[tkt[0]] = tkt[1]
    if tkt[0] == None:
      route[0] = tkt[1]
  for i in range(1, len(route)):
    if route[i-1] in tkt_dict:
      route[i] = tkt_dict[route[i-1]]
    else:
      return []
  return route


  # trip = []
  # for tkt in tickets:
  #   if tkt[0] == None:
  #     trip.append(tkt)
  #   else:
  #     return trip
  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
