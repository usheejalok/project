print"hello"
print 'Let\a get started'
spy_name=raw_input('what is your spy name..!!')

if len(spy_name)>2:
    print  'welcome '  + spy_name +  '. Glad to have you back with us.'
    spy_salution = raw_input("what should we call you(Mr. or Ms.)?")
    if spy_salution=="Mr."  or spy_salution=="Ms." or spy_salution=="mr." or spy_salution=="ms.":

        spy_name = spy_salution + "" + spy_name
        print "alright " + spy_name + ". I would like to know a little bit about you"
        spy_age = 0
        spy_raiting = 0.0
        spy_is_online = True
        spy_age = input('what is your age?')
        if 30>spy_age>15:
            print "your age is correct"
            spy_raiting = input('what is your Rating out of 10?')
            if spy_raiting>5.0:
                print "great spy A+ grade"
            elif 3.5<spy_raiting<=5.0:
                print "average spy B grade"
            elif 2.5<spy_raiting<=3.5:
                print "ok ok spy c grade"
            else:
                print " not valid spy? "
            spy_is_online = True
            print"authentication complete,WELCOME " + spy_name + "age:" + str(spy_age) + "and rating of: +str(spy_rating) " + "proud to have u"
        else:
            print "you are not eligible for spy..!!"


    else:
        print "invalid salution"

else:
    "Please enter a valid name"