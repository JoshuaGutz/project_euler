# # 151 Paper sheets of standard sizes: an expected-value problem

# find the expected number of times (during each week) that the foreman 
# finds a single sheet of paper in the envelope

import random

def instructions():
    # A printing shop runs 16 batches (jobs) every week and each batch 
    # requires a sheet of special colour-proofing paper of size A5.
    
    # Every Monday morning, the foreman opens a new envelope, containing 
    # a large sheet of the special paper with size A1.
    
    # He proceeds to cut it in half, thus getting two sheets of size A2. 
    # Then he cuts one of them in half to get two sheets of size A3 and 
    # so on until he obtains the A5-size sheet needed for the first 
    # batch of the week.
    
    # All the unused sheets are placed back in the envelope.
    
    # At the beginning of each subsequent batch, he takes from the 
    # envelope one sheet of paper at random. If it is of size A5, he 
    # uses it. If it is larger, he repeats the 'cut-in-half' procedure 
    # until he has what he needs and any remaining sheets are always 
    # placed back in the envelope.
    
    # Excluding the first and last batch of the week, find the expected 
    # number of times (during each week) that the foreman finds a single 
    # sheet of paper in the envelope.
    
    # Give your answer rounded to six decimal places using the format 
    # x.xxxxxx .
    pass
pass

def batches_remaining(envelope): # envelope is list of 5 1's or 0's
    batches_remaining = 0
    for i in range(len(envelope)):
        batches_remaining += envelope[i] * 2 ** i
    return batches_remaining
pass

def test_prints():
    #          [#A5's, #A4's, #A3's, #A2's, #A1's]
    #          [#1's,  #2's,  #4's,  #8's,  #16's]
    envelope = [ 0,     0,     0,     0,      1] # before batch 1
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 1,     1,     1,     1,      0] # after batch 1
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 1,     1,     0,     1,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 1,     0,     1,     1,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 0,     1,     1,     1,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 1,     1,     1,     0,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 2,     2,     2,     0,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 3,     3,     1,     0,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 7,     1,     0,     0,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
    envelope = [ 8,     0,     0,     0,      0]
    print batches_remaining(envelope), envelope, sum(envelope)
# test_prints()

def the_scenario():
    # sum(envelope) == number of sheets in the envelope
    envelope = [ 0,     0,     0,     0,      1] # before batch 1
    envelope = [ 1,     1,     1,     1,      0] # after batch 1
    count = 0
    # print batches_remaining(envelope), envelope
    while batches_remaining(envelope) > 1:
        if sum(envelope) == 1: # number of sheets in envelope
            count += 1
            # print "count =", count
        sheet = random.randint(1, sum(envelope))
        if sheet <= sum(envelope[0:1]): # if sheet is a '1'
            # print "picked a 2^0 = 1"
            envelope[0] -= 1
        elif sheet <= sum(envelope[0:2]): # if sheet is a '2'
            # print "picked a 2^1 = 2"
            envelope[0] += 1
            envelope[1] -= 1
        elif sheet <= sum(envelope[0:3]): # if sheet is a '4'
            # print "picked a 2^2 = 4"
            envelope[0] += 1
            envelope[1] += 1
            envelope[2] -= 1
        elif sheet <= sum(envelope[0:4]): # if sheet is a '8'
            # print "picked a 2^3 = 8"
            envelope[0] += 1
            envelope[1] += 1
            envelope[2] += 1
            envelope[3] -= 1
        # print batches_remaining(envelope), envelope
    # print "\n count =", count
    return count
# print the_scenario()

def run_infinite_times():
    scenario = 0
    total = 0
    while True:
        outcome = the_scenario()
        scenario += 1
        total += outcome
        print outcome, scenario, total / float(scenario)
    pass
# run_infinite_times()

def another_example():
    # Start by figuring out your odds of each number of times:
    # XXX is unique scenarios that could happen
    # A + B + C + D = XXX #(side note: A > B > C > D)
    # There's a A = A in XXX chance that it'll be 0 
    # There's a B = B in XXX chance that it'll be 1
    # There's a C = C in XXX chance that it'll be 2
    # There's a D = 1 in XXX chance that it'll be 3
    # expected value is (0 * A + 1 * B + 2 * C + 3 * D) / XXX
    # or (B + 2 * C + 3) / XXX
    # XXX is unique ways to turn [1,1,1,1,0] into [1,0,0,0,0]
    pass
pass
