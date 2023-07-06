# importing the libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import openpyxl


# load the files

df = pd.read_excel("Subs.xlsx")
df1 = pd.read_excel("Revenue_netflix.xlsx")
df2 = pd.read_excel("content.xlsx")
df3 = pd.read_excel("net_profit.xlsx")
df4 = pd.read_excel("netflix_region.xlsx")
df5 = pd.read_excel("demographics.xlsx")
df6 = pd.read_excel("Penteration.xlsx")
df7 = pd.read_excel("average spent hours.xlsx")
df8 = pd.read_excel("Best Movie by Year Netflix.xlsx")
df9 = pd.read_excel("ott_subs.xlsx")
df10 = pd.read_csv("Netflix_Cleaned.csv")

#  for title
st.title("Data Discoveries: Inside Netflix")
st.sidebar.image('netflix.jpg', use_column_width=True)  # import image

# create sidebar and dropdown

dropdown = ['Netflix History', 'Netflix Overview Insights', 'Netflix Subscribers', 'Netflix Revenue', 'Content Spend',
            'Net Profit',
            'Netflix Subscriber by Region', 'Netflix Demographics', 'Netflix Penetration Rate', 'Average Spent Hours',
            'Best Movie by Year', 'Netflix Statistics', 'Netflix Vs The Competition']
buttons = st.sidebar.selectbox('Data Discoveries: Inside Netflix', dropdown)
st.sidebar.write("You selected:", buttons)

# creating a button
b = st.sidebar.button('Netflix Insights')

# EDA
if b:
    if buttons == 'Netflix History':
        st.write("1.Foundation (1997-2000):Netflix was founded in 1997 by Reed Hastings and Marc Randolph. Initially, "
                 "it started as a DVD-by-mail rental service, allowing customers to rent DVDs online and have them "
                 "delivered to their homes.")

        st.write("2.Transition to Streaming (2007-2010):In 2007, Netflix introduced its online streaming service, "
                 "allowing subscribers to stream content directly to their computers. The company made a strategic "
                 "shift from primarily focusing on DVD rentals to a digital streaming platform.")

        st.write("3.Expansion and Original Content (2012-2013):Netflix started expanding its streaming service to "
                 "international markets, launching in Canada in 2010 and gradually expanding to other countries. In "
                 "2012, Netflix released its first original series, 'Lily-hammer',marking the beginning of its "
                 "venture into producing original content.")

        st.write("4.Global Dominance (2016-2017):By 2016, Netflix had expanded its streaming service to over 190 "
                 "countries, becoming a global entertainment platform. The company continued to invest heavily in "
                 "producing original content, including popular series such as 'Stranger Things', 'Narcos', "
                 "and 'The Crown'")

        st.write("5.Continued Growth (2018-Present):In recent years, Netflix has continued its growth and dominance "
                 "in the streaming industry. It has expanded its library of original content, including films, "
                 "series, documentaries, and stand-up comedy specials. The company has also entered into partnerships "
                 "with renowned filmmakers and production houses, further strengthening its position in the market.")

        st.write("Today, Netflix remains one of the leading streaming platforms globally, with millions of "
                 "subscribers and a vast library of diverse content. It continues to innovate and adapt to changing "
                 "viewer preferences, shaping the landscape of digital entertainment.")
    elif buttons == 'Netflix Subscribers':
        fig = px.line(df, df['Year'], df['Subscriber'], markers=True, title='Netflix Subscriber in Millions')
        st.plotly_chart(fig)
    elif buttons == 'Netflix Revenue':
        fig1 = px.bar(df1, df1['Year'], df1['Revenue'], text_auto='.2s', title='Netflix Revenue in ($bn)')
        st.plotly_chart(fig1)
    elif buttons == 'Content Spend':
        fig2 = px.bar(df2, df2['Year'], df2['Content Spend'], text_auto='.2s', title='Netflix Content Spend in ($bn)')
        st.plotly_chart(fig2)
    elif buttons == 'Net Profit':
        fig3 = px.bar(df3, df3['year'], df3['Net Income'], text_auto='.2s', title='Netflix Net Profit in ($Mm)')
        st.plotly_chart(fig3)
    elif buttons == 'Netflix Subscriber by Region':
        fig4 = make_subplots(rows=2, cols=2, start_cell='bottom-left',
                             subplot_titles=('Netflix Subscribers by US & Canada',
                                             'Netflix Subscribers by Latin America',
                                             'Netflix Subscribers by EMEA',
                                             'Netflix Subscribers by Asia-Pacific'))
        fig4.add_trace(go.Bar(x=df4['Year'], y=df4['US & Canada'], name='US & Canada'), row=1, col=1)
        fig4.add_trace(go.Bar(x=df4['Year'], y=df4['Latin America'], name='Latin America'), row=1, col=2)
        fig4.add_trace(go.Bar(x=df4['Year'], y=df4['EMEA'], name='EMEA'), row=2, col=1)
        fig4.add_trace(go.Bar(x=df4['Year'], y=df4['Asia-Pacific'], name='Asia-Pacific'), row=2, col=2)
        fig4.update_layout(title='Netflix Subscriber by Region in (Mm)')
        st.plotly_chart(fig4)
    elif buttons == 'Netflix Demographics':
        fig5 = px.pie(df5, values='Percentage Of Users', names='Gender', title='Netflix Demographics',
                      color_discrete_map={'Male': 'lightcyan',
                                          'Female': 'darkblue',
                                          })
        st.plotly_chart(fig5)
    elif buttons == 'Netflix Penetration Rate':
        st.write("The penetration rate is one of the best measurements to see how successful Netflix has been in"
                 "individual countries.The penetration rate is the percentage of the relevant total population that"
                 " has purchased a Netflix subscription at least once")
        fig6 = px.bar(df6, df6['Country'], df6['Penetration Rate'], title='Netflix Penetration Rate (%)')
        st.plotly_chart(fig6)
    elif buttons == 'Average Spent Hours':
        fig7 = px.line(df7, df7['Year'], df7['Average Daily Time Per Subscriber (Global)'],
                       title='Average Spent Hours in Netflix')
        st.plotly_chart(fig7)
        st.write('This was due to the COVID-19 pandemic in 2020. People spent much more time in their homes and '
                 'therefore consumed more streaming content in general.')
    elif buttons == 'Best Movie by Year':
        st.header('Best Movie by Year')
        st.dataframe(df8)
    elif buttons == 'Netflix Statistics':
        st.write('1.Netflix generated $31.6 billion revenue in 2022, a 6.7% increase on the previous year.')
        st.write("2.In Netflix Movie content is more than Tv Show")
        st.write("3.In 2018  most movie has  released")
        st.write("4.In United States most movie/Tv Show has released")
        st.write('5.Most Movies/Tv shows Has TV-MA Ratings')
        st.write("6.Netflix generated 220.6 million subscriber in 2022, a5% increase on the previous year")
        st.write(
            "7.Netflix made $4.4 billion net profit in 2022, the company’s first decline in net income since 2012.")
        st.write("8.The Europe, Middle East & Africa market surpassed the United States & Canada for subscribers in "
                 "2022.")
        st.write("9.Netflix slightly decreased its content spend in 2022, from $17.7 billion to $16.8 billion.")
        st.write("10.The company reported that its users are 49% women and 51% men.This is extremely balanced for any "
                 "streaming platform.")
        st.write("11.Netflix has the highest penetration rate in Australia overall..")
    elif buttons == 'Netflix Vs The Competition':
        st.write("It’s no secret that Netflix now has some serious competition:")
        st.write("1.Disney+")
        st.write("2.HBO Max")
        st.write("3.Hulu")
        st.write("4.Amazon Prime")
        st.write("5.Apple TV Plus")
        st.write("There are tons of streaming platforms available to consumers offering lots of different content. "
                 "And some of these new competitors are backed by massive multi-billion dollar companies.")

        st.write("The truth is that most of Netflix’s competitors just copied their model and used it as a blueprint. "
                 "But the reality is that it worked, and Netflix has struggled to maintain its subscriber value – "
                 "especially because Netflix is more expensive.So the big question is can Netlfix continue to be the "
                 "top dog?Here are the latest Netflix statistics you need to know about their competition.")
        st.write("Netflix Is Losing Subscribers 2022 has not been a good year for Netflix.It’s the first year that "
                 "Netflix has had a downturn in subscribers. Every year prior has been continuous growth for the "
                 "company.Netflix posted a big earnings miss in the first quarter of 2022 as it reported losing 200,"
                 "000 subscribers. Things only got worse in the second quarter of 2022 as Netflix reported another "
                 "loss of 1 million subscribers.")

        st.write("This is the direct opposite of the constant growth the platform wants to see and was expected by "
                 "investors.Market experts weren’t as surprised because of the rise in competition. I mean, "
                 "at some point, they would start to have a looser grip on the market, right?But Netflix isn’t "
                 "backing down.")
        st.write("1..The platform is planning to jumpstart growth by:Creating a new ads-supported")
        st.write(
            "2.ServiceTargeting password sharingA recent study estimated password sharing was costing Netflix $6" "billion in revenue per year.")
        st.write("Crazy, right?We will have to wait and see if it’s enough to stop the "
                 "bleeding.")

        st.write("Netflix Is Becoming Too Expensive.")
        st.write("1.The truth is that Netflix is becoming more and more expensive.")
        st.write("2.The online streaming giant has constantly increased prices since 2011." "When it first launched,"
                 "it was just $7.99 per month.")
        st.write("The premium Netflix subscription, which offers 4 ""screens playing " "simultaneously (a common plan "
                 "for families), "
                 "is $20 per month.Netflix has turned ""from “value for ""money” to a “premium” subscription for most "
                 "users.")
        st.write("The big problem is that Netflix is far more expensive than top competitors:")
        st.write("1.Disney Plus – $8 per month")
        st.write("2.Apple TV Plus – $5 per month")
        st.write("3.Hulu (No Ads) – $13 per month")
        st.write("4.HBO Max (No Ads) – $15 per month")
        st.write("5.Amazon Prime Video – $9 per month")

        st.write(" Netflix Has The “Worst” Content")
        st.write("But the big definer on price is the quality of content.")
        st.write("Here’s the truth:")
        st.write("At the moment, the online streaming market is dominated by series. If you can produce great series "
                 "consistently, you will hold onto your subscribers.")
        st.write("Unfortunately, over the last year, Netflix hasn’t been able to produce enough of them.If you are "
                 "after relevant and binge-worthy series, Netflix’s offerings have only seemed to worsen. Especially "
                 "when you compare it to competitors.")
        st.write("That’s not to say that Netflix has no good shows. But you are paying a premium price for a lot of "
                 "general content. This is directly opposite to a platform like Apple TV Plus, which only offers "
                 "premium content.")
        st.write("think of it like a quantity vs quality situation.")
        st.write("Other streaming platforms like Disney Plus have also focussed on developing their platform content "
                 "offerings.")

        st.write("When it first launched, Disney Plus had a considerable amount of content for children but lacked "
                 "quality content for adults.")
        st.write("But Netflix Still Dominate The Market In Term Of Subscribers (For Now)Even though Netflix declined "
                 "in subscribers – They are still at the top of the streaming market (for now at least).")
        st.dataframe(df9)
    elif buttons == 'Netflix Overview Insights':
        df11 = df10['release_year'].value_counts().reset_index().rename(
            columns={"total_movie": "Year", "count": "total_movie"})
        fig = px.bar(df11, df11["release_year"], df11["total_movie"], title='Total movies released in Each Year')
        st.plotly_chart(fig)

        df12 = df10['type'].value_counts().reset_index().rename(columns={'index': 'Type', 'type': 'Total_count'})
        fig = px.pie(df12, values='count', names='Total_count', title='Shows Type',
                     color_discrete_map={'Movie': 'lightcyan',
                                         'TV Show': 'darkblue',
                                         })
        st.plotly_chart(fig)

        df13 = df10['country'].value_counts().reset_index().rename(
            columns={'index': 'country', 'country': 'Total_movies'}).head(10)
        fig = px.treemap(df13, names=df13['Total_movies'], parents=["" for _ in df13['Total_movies']], values=df13['count'],
                         title="Top 10 countries where most movies/shows released ")
        st.plotly_chart(fig)

        df14 = df10['rating'].value_counts().reset_index().rename(columns={'index': "rating", "rating": 'total_count'})
        fig = px.bar(df14, x='total_count', y='count', title='Movie Ratings Distribution', text_auto=True)
        st.plotly_chart(fig)


        st.text("Most Common  words in Geners")
        x = df10['listed_in'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        st.text("Most Common  words in description")
        x = df10['description'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        st.text("Most Common  words in cast")
        x = df10['cast'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
