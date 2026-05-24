import streamlit as st
import streamlink 

st.set_page_config(layout="wide")
st.title("Live Youtube Streaming")
 

youtube_url = ["https://www.youtube.com/watch?v=O61gbmYZJmE",
                "https://www.youtube.com/watch?v=UrsmFxEIp5k",
                "https://www.youtube.com/watch?v=O9v10jQkm5c",
                "https://www.youtube.com/watch?v=28u7FhEWxyg",
                "https://www.youtube.com/watch?v=s0LLVQeMmtU"
               ]


def get_stream_url(youtube_url):

    try:
        streams = streamlink.streams(youtube_url)

        if "best" in streams:
            return streams["best"].url
        return None

    except Exception as e:
        st.error(f"Error loading stream: {e}")
        return None

# Create 2 columns

col1, col2 = st.columns(2)


# Stream 1

with col1:

    st.subheader("Live Stream 1")

    stream_url = get_stream_url(youtube_urls[0])

 

    if stream_url:

        st.video(stream_url)

 

# Stream 2

with col2:

    st.subheader("Live Stream 2")

    stream_url = get_stream_url(youtube_urls[1])

 

    if stream_url:

        st.video(stream_url)

 

# Second row

col3, col4 = st.columns(2)

 

# Stream 3

with col3:

    st.subheader("Live Stream 3")

    stream_url = get_stream_url(youtube_urls[2])

 

    if stream_url:

        st.video(stream_url)

# Stream 4

with col4:

    st.subheader("Live Stream 4")

    stream_url = get_stream_url(youtube_urls[3])

 

    if stream_url:

        st.video(stream_url)


