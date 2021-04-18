
# Setup
yes_no = ["yes", "no"]

answer=input('there are aliens invading earth and you are the earths leader \n' \
                                'choose what to do: \n' \
                                '1) Declare war on the aliens \n' \
                                '2) Get peace with the aliens \n :')



if answer=='1':
    print('You choosed war without declaration!')
    print('The war begins')
    print('We won! :)')
elif answer=='2':
    print('You choosed peace.')
    print('But the aliens choosed war without declaration!')
    print('The earth is overtaken! :(')
else:
    print('Choose 1 or 2')
