import streamlit as st
import streamlink 

st.set_page_config(layout="wide")
st.title("Live Youtube Streaming")
 

youtube_url = ["https://www.youtube.com/watch?v=O61gbmYZJmE",
                "https://www.youtube.com/watch?v=UrsmFxEIp5k",
                "https://www.youtube.com/watch?v=O9v10jQkm5c",
                "https://www.youtube.com/watch?v=28u7FhEWxyg",
                "https://www.primevideo.com/region/eu/detail/0RV81WUUHUNK1H2SSUO4FFF6T5/ref=atv_hm_hom_c_cjm7wb_3_2?jic=8%7CEgNhbGw%3D",
                "https://www.netflix.com/watch/82813816?trackId=254015180&tctx=0%2C0%2C32d8ffd3-367b-4d08-9fc3-11a4d260dcb4-175022200%2CNES_946256CF41107CBC4D928DCBBDEDDD-E911D54DEEF141-B11BB753AC_p_1779635628453%2CNES_946256CF41107CBC4D928DCBBDEDDD_p_1779635628453%2C%2C%2C%2C%2CVideo%3A82813816%2CbillboardPlayButton"
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

    stream_url = get_stream_url(youtube_url[0])

 

    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")
 

# Stream 2

with col2:

    st.subheader("Live Stream 2")

    stream_url = get_stream_url(youtube_url[1])

 

    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")
 

# Second row

col3, col4 = st.columns(2)

 

# Stream 3

with col3:

    st.subheader("Live Stream 3")

    stream_url = get_stream_url(youtube_url[2])

 

    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")
# Stream 4

with col4:

    st.subheader("Live Stream 4")

    stream_url = get_stream_url(youtube_url[3])

 

    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")


col5, col6 = st.columns(2)


with col5:

    st.subheader("Live Stream 5")

    stream_url = get_stream_url(youtube_url[4])


    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")    

with col6:

    st.subheader("Live Stream 6")

    stream_url = get_stream_url(youtube_url[5])


    if stream_url:

        st.video(stream_url)
    else:
     st.warning("Unable to load stream")
