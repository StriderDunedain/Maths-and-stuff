print('Welcome to the solver of quadric equations! (and inequations)')  
               
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

D = b**2 - 4*a*c
  
if D < 0:
  print('No answer!')
  print('Discriminant < 0')  
else:
  print('Discriminant = ' + str(D))
  x_1 = (-b + D**0.5) / (2*a)
  x_2 = (-b - D**0.5) / (2*a)
  f = len(str(x_1))
  h = len(str(x_2))
  
  if h > 5 and f > 5:
      var = round(x_1, 3)
      var_ = round(x_2, 3)
      print('x1 = {xf} and x2 = {xs}'.format(xf=var, xs=var_))
  elif f > 5:
      var = round(x_1, 3)
      print('x1 = {xf} and x2 = {xs}'.format(xf=var, xs=x_2))
  elif h > 5:
      var = round(x_2, 3)
      print('x1 = {xf} and x2 = {xs}'.format(xf=x_1, xs=var))
  else:
      print('x1 = ' + str(x_1) + ' and x2 = ' + str(x_2))
      
subst = (-b + D**0.5) / (2*a)
subst2 = (-b - D**0.5) / (2*a)
rooted_lst = [1.4142135623730951, 1.7320508075688772,
              2.23606797749979, 2.449489742783178,
              2.6457513110645907, 2.8284271247461903,
              3.1622776601683795, 3.3166247903554,
              3.4641016151377544, 3.605551275463989,
              3.7416573867739413, 3.872983346207417,
              4.123105625617661, 4.242640687119285,
              4.358898943540674, 4.47213595499958,
              4.58257569495584, 4.69041575982343,
              4.795831523312719, 4.898979485566356,
              5.0990195135927845, 5.196152422706632,
              5.291502622129181, 5.385164807134504,
              5.477225575051661, 5.5677643628300215,
              5.656854249492381, 5.744562646538029,
              5.830951894845301, 5.916079783099616,
              6.082762530298219, 6.164414002968976,
              6.244997998398398, 6.324555320336759,
              6.4031242374328485, 6.48074069840786,
              6.557438524302, 6.6332495807108,
              6.708203932499369, 6.782329983125268,
              6.855654600401044, 6.928203230275509,
              7.0710678118654755, 7.14142842854285,
              7.211102550927978, 7.280109889280518,
              7.3484692283495345, 7.416198487095663,
              7.483314773547883, 7.54983443527075,
              7.615773105863909, 7.681145747868608,
              7.745966692414834, 7.810249675906654,
              7.874007874011811, 7.937253933193772,
              8.06225774829855, 8.12403840463596,
              8.18535277187245, 8.246211251235321,
              8.306623862918075, 8.366600265340756,
              8.426149773176359, 8.48528137423857,
              8.54400374531753, 8.602325267042627,
              8.660254037844387, 8.717797887081348,
              8.774964387392123, 8.831760866327848,
              8.888194417315589, 8.94427190999916,
              9.055385138137417, 9.1104335791443,
              9.16515138991168, 9.219544457292887,
              9.273618495495704, 9.327379053088816,
              9.38083151964686, 9.433981132056603,
              9.486832980505138, 9.539392014169456,
              9.591663046625438, 9.643650760992955,
              9.695359714832659, 9.746794344808963,
              9.797958971132712, 9.848857801796104,
              9.899494936611665, 9.9498743710662]

if (subst2 in rooted_lst) == True:
    strx = subst2**2
    x_2 = '√' + str(round(strx))
    x_1 = '-√' + str(round(strx))
if (subst in rooted_lst) == True:
    strx = subst**2
    x_1 = '√' + str(round(strx))
    x_2 = '-√' + str(round(strx))

exp1 = 'The answer to the inequality are the combined periods of (-infinity ; {sec_x}) U ({fst_x} ; +infinity)'.format(sec_x = x_2, fst_x = x_1)
exp2 = 'The answer to the inequality is the period between ({sec_x} ; {fst_x})'.format(sec_x = x_2, fst_x = x_1)
exp3 = 'The answer to the inequality are combined periods of (-infinity ; {sec_x}] U [{fst_x} ; +infinity)'.format(sec_x = x_2, fst_x = x_1)
exp4 = 'The answer to the inequality is the period between [{sec_x} ; {fst_x}]'.format(sec_x = x_2, fst_x = x_1)

exp_1 = 'The answer to the inequality are the combined periods of (-infinity ; {}) U ({} ; +infinity)'.format(x_1, x_2)
exp_2 = 'The answer to the inequality is the period between ({} ; {})'.format(x_1, x_2)
exp_3 = 'The answer to the inequality are combined periods of (-infinity ; {}] U [{} ; +infinity)'.format(x_1, x_2)
exp_4 = 'The answer to the inequality is the period between [{} ; {}]'.format(x_1, x_2)

zero_c = 'The answer to the inequality is the period between (-infinity ; +infinty)'
zero_c_1 = 'The answer to the inequality is just one number - {}'.format(x_1)
zero_c_2 = 'There are no answers to this inequality'
zero_c_3 = 'The answer to the inequality are combined periods of (-infinity ; {in_zero}) U ({in_zero} ; +infinity)'.format(in_zero=x_1)

def first_outcome(a, b, c):
    less = input('Is the sign "<"?')
    if less == '1':
        print(exp2)  
    else:
        more = input('Is the sign ">"?')
        if more == '1':
            print(exp1)
        else:
            more_or_equal = input('Is the sign ">="?')
            if more_or_equal == '1':
                print(exp3)
            else:
                less_or_equal = input('Is the sign "=<"?')
                if less_or_equal == '1':
                    print(exp4)
                else:
                    print('What? How?! I mean, we tried all signs')

def second_outcome(a, b, c):
    less_ = input('Is the sign "<"?')
    if less_ == '1':
        print(exp1)  
    else:
        more_ = input('Is the sign ">"?')
        if more_ == '1':
            print(exp2)
        else:
            more_and_equal = input('Is the sign ">="?')
            if more_and_equal == '1':
                print(exp4)
            else:
                less_and_equal = input('The is sign "=<"?')
                if less_and_equal == '1':
                    print(exp3)
                else:
                    print('What? How?! I mean, we tried all signs')

def third_outcome(a, b, c):
    less = input('Is the sign "<"?')
    if less == '1':
        print(exp_2)  
    else:
        more = input('Is the sign ">"?')
        if more == '1':
            print(exp_1)
        else:
            more_or_equal = input('Is the sign ">="?')
            if more_or_equal == '1':
                print(exp_3)
            else:
                less_or_equal = input('Is the sign "=<"?')
                if less_or_equal == '1':
                    print(exp_4)
                else:
                    print('What? How?! I mean, we tried all signs')

def fourth_outcome(a, b, c):
    less_ = input('Is the sign "<"?')
    if less_ == '1':
        print(exp_1)  
    else:
        more_ = input('Is the sign ">"?')
        if more_ == '1':
            print(exp_2)
        else:
            more_and_equal = input('Is the sign ">="?')
            if more_and_equal == '1':
                print(exp_4)
            else:
                less_and_equal = input('The is sign "=<"?')
                if less_and_equal == '1':
                    print(exp_3)
                else:
                    print('What? How?! I mean, we tried all signs')
                    
def equal_outcome(a, b, c):
    less_ = input('Is the sign "<"?')
    if less_ == '1':
        print(zero_c_2)  
    else:
        more_ = input('Is the sign ">"?')
        if more_ == '1':
            print(zero_c_3)
        else:
            more_and_equal = input('Is the sign ">="?')
            if more_and_equal == '1':
                print(zero_c)
            else:
                less_and_equal = input('The is sign "=<"?')
                if less_and_equal == '1':
                    print(zero_c_1)
                else:
                    print('What? How?! I mean, we tried all signs') 

def equal_outcome_two(a, b, c):
    less_ = input('Is the sign "<"?')
    if less_ == '1':
        print(zero_c_3)  
    else:
        more_ = input('Is the sign ">"?')
        if more_ == '1':
            print(zero_c_2)
        else:
            more_and_equal = input('Is the sign ">="?')
            if more_and_equal == '1':
                print(zero_c_1)
            else:
                less_and_equal = input('The is sign "=<"?')
                if less_and_equal == '1':
                    print(zero_c)
                else:
                    print('What? How?! I mean, we tried all signs')

if subst > subst2:
    stage = subst2 - 1
    equation = a * stage**2 + b*stage + c
    if equation > 0:
        first_outcome(a, b, c)
    elif equation < 0:
        second_outcome(a, b, c)
elif subst2 > subst:
    stage = subst - 1
    equation = a * stage**2 + b*stage + c
    if equation > 0:
        third_outcome(a, b, c)
    elif equation < 0:
        fourth_outcome(a, b, c)
elif subst == subst2:
    stage = subst - 1
    equation = a * stage**2 + b*stage + c
    if equation > 0:
        equal_outcome(a, b, c)
    elif equation < 0:
        equal_outcome_two(a, b, c)
else:
    print('Sorry, something went wrong. Maybe you skipped the signs?')
    print('If u did this on purpose then yes, this message exists')
    print('Btw if you DID do this on purpose then I have just one question: "How tf bored are you in order to do this?!"')
ignore = input('Ignore')
