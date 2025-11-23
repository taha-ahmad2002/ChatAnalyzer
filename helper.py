from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud


def fetch_stats(selected_user,df):
        if selected_user!='Overall':
            df=df[df['user']==selected_user]
        # 1. fetch number of messages
        num_messages=df.shape[0]
        # 2. number of words
        words=[]
        for message in df['messages']:
            words.extend(message.split())

        # fetch number of media messages
        num_media_messages=df[df['messages']=='<Media omitted>\n'].shape[0]

        #fetch number of links shared
        links=[]
        for message in df['messages']:
            links.extend(extract.find_urls(message))



        # fetch number of shared links
        return num_messages,len(words),num_media_messages,len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    df=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'user': 'name', 'count': 'percentage'})
    return x,df

def create_wordcloud(selected_user,df):
    if selected_user!='Overall':
        df=df[df['user']==selected_user]

    wc= WordCloud(width=800, height=800, background_color='white',min_font_size=20)
    df_wc=wc.generate(df['messages'].str.cat(sep=' '))
    return df_wc