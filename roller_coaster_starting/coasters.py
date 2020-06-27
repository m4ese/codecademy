import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
def load_data():
    wood_winners = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
    steel_winners = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
    return wood_winners,steel_winners


# write function to plot rankings over time for 1 roller coaster here:
def rankings_v_time(coaster_name,ranker,park_name):
    coaster_info = ranker[(ranker.Name == coaster_name) & (ranker.Park == park_name)]
    
    years = coaster_info['Year of Rank']
    rankings = coaster_info.Rank
    
    plt.plot(years,rankings,marker='*')
    plt.show()  
    
    plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def two_coasters(coaster_1,coaster_2,park_1,park_2,ranker_df):
    rankings_v_time(coaster_1,ranker,park_1)
    rankings_v_time(coaster_2,ranker,park_2)









plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
