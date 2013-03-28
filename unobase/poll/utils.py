'''
Created on 26 Mar 2013

@author: michael
'''

def get_poll_percentages(poll_answers):
    total_vote_counts = 0.0
    vote_count_averages = []
    
    for poll_answer in poll_answers:
        total_vote_counts += poll_answer.vote_count
    
    for poll_answer in poll_answers:
        try:
            vote_count_averages.append(float('%0.2f' % ((poll_answer.vote_count / total_vote_counts) * 100)))
        except ZeroDivisionError:
            vote_count_averages.append(0.0)
    
    return vote_count_averages