class ParsingTable:
  def __init__(self):
      self.parse_table = [[0] * 11 for _ in range(7)]
      for i in range(7):
          self.parse_table[i][0] = 0
      for i in range(11):
          self.parse_table[0][i] = 0
      self.parse_table[1][1] = 1
      self.parse_table[2][2] = 21
      self.parse_table[2][3] = 22
      self.parse_table[2][8] = 23
      self.parse_table[3][4] = 31
      self.parse_table[3][5] = 32
      self.parse_table[3][9] = 100
      self.parse_table[3][10] = 101
      self.parse_table[4][2] = 41
      self.parse_table[4][3] = 42
      self.parse_table[4][8] = 43
      self.parse_table[5][4] = 102
      self.parse_table[5][5] = 103
      self.parse_table[5][6] = 51
      self.parse_table[5][7] = 52
      self.parse_table[5][9] = 104
      self.parse_table[5][10] = 105
      self.parse_table[6][2] = 200
      self.parse_table[6][3] = 201
      self.parse_table[6][8] = 202

  def get(self, row, col):
      return self.parse_table[row][col]

def convert_to_row(c):
  if c == 'S':
      return 1
  elif c == 'E':
      return 2
  elif c == 'Q':
      return 3
  elif c == 'T':
      return 4
  elif c == 'R':
      return 5
  elif c == 'F':
      return 6
  else:
      return 0

def convert_to_col(c):
  if c == '@':
      return 1
  elif c == 'a':
      return 2
  elif c == 'b':
      return 3
  elif c == '+':
      return 4
  elif c == '-':
      return 5
  elif c == '*':
      return 6
  elif c == '/':
      return 7
  elif c == '(':
      return 8
  elif c == ')':
      return 9
  elif c == '$':
      return 10
  else:
      return 0

def push_back_to_stack(st, x):
  if x == 0:
      return False
  #checks for the a=E and pushes onto stack returns true to continue 
  if x == 1:
      print("Pushing a=E onto the stack.")
      st.append('E')
      st.append('@')  
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
    #checks for the TQ and pushes onto stack true to continue
  elif x == 21 or x == 22 or x == 23:
      print("Pushing TQ onto the stack.")
      st.append('Q')
      st.append('T')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
    
      return True
  elif x == 31:
      print("Pushing +TQ onto the stack.")
      st.append('Q')
      st.append('T')
      st.append('+')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 32:
      print("Pushing -TQ onto the stack.")
      st.append('Q')
      st.append('T')
      st.append('-')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 100 or x == 101 or x == 102 or x == 103 or x == 104 or x == 105:
      print("Pushing ^ (Lambda) onto the stack.")
      st.append('^')  # ^ -> lambda
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 41 or x == 42 or x == 43:
      print("Pushing FR onto the stack.")
      st.append('R')
      st.append('F')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 51:
      print("Pushing *FR onto the stack.")
      st.append('R')
      st.append('F')
      st.append('*')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 52:
      print("Pushing /FR onto the stack.")
      st.append('R')
      st.append('F')
      st.append('/')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 200:
      print("Pushing 'a' onto the stack.")
      st.append('a')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 201:
      print("Pushing b onto the stack.")
      st.append('b')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  elif x == 202:
      print("Pushing (E) onto the stack.")
      st.append(')')
      st.append('E')
      st.append('(')
      print("Current stack:", end=' ')
      for item in st:
          print(item, end=' ')
      print()
      return True
  else:
      return False

def main():
  parse_table = ParsingTable()
  input_string = input("Enter string: ")

  # char to hold position 
  state = ''

  # check to see if input is valid 
  accepted = True

  # initalized list to start off on 
  st = ['$','S']

  # gets input 
  print("Input string:", input_string)
  while len(st) > 0:
      state = st[-1]

      # read the input and puts the next character 
      input_char = input_string[0]

      next_char = input_string[1] if len(input_string) > 1 else ''
      if next_char == '=':
          input_char = '@'

      # pop from stack if lambda 
      if state == '^':
          print("Popping ^ (Lambda) from the stack.")
          st.pop()
          print("Current stack:", end=' ')
          for item in st:
              print(item, end=' ')
          print()

    #checks everything else that isnt $ and pops, also checks input_char to see if it needs to be rejected or accepted
      elif state in '@ab+()$-*/':
          if state == input_char:
              if state == '@':
                #pop to check for @
                  print("Popping from stack: @(a=)")
                  st.pop()
                  input_string = input_string[2:]
              else:
                  print("Popping from stack:", st[-1])
                  st.pop()
                  input_string = input_string[1:]
              print("Input:", input_string)
          else:
              print("Rejected.")
              accepted = False
              break

      # If state is non-terminal  then retrieve the states from the parsing table.

    #If state is non-term then pop and push 
      elif state in 'SETQFR':
          row = convert_to_row(state)
          col = convert_to_col(input_char)
          new_state = parse_table.get(row, col)
          print("Popping from stack:", st[-1])
          st.pop()
          print("Current stack:", end=' ')
          for item in st:
              print(item, end=' ')
          print()
          if not push_back_to_stack(st, new_state):
              accepted = False
              break

  if accepted:
      print("accepted")
  else:
      print("rejected")

if __name__ == '__main__':
  main()
