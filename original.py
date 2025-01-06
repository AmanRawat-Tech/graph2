import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import streamlit as st
st.set_page_config(
    layout='wide'
) 
def plot_dynamic_data_multiple_msn(msn_filters, date_filter, column_filter):
    data=pd.read_excel('odata.xlsx')
    # Create a dataframe from the provided data
    df = pd.DataFrame(data, columns=['msn', 'ts', 'v_ave', 'i_ave', 'wh_imp', 'vah_imp'])
 
    # Convert ts to datetime type
    df['ts'] = pd.to_datetime(df['ts'])
 
    # Extract time from ts in hh:mm:ss format
    df['time'] = df['ts'].dt.strftime('%H:%M:%S')
 
    # Filter data by multiple msns and date
    filtered_data = df[(df['msn'].isin(msn_filters)) & (df['ts'].dt.date == pd.to_datetime(date_filter).date())]
 
    # Ensure the column exists in the filtered data
    if column_filter not in filtered_data.columns:
        print(f"Error: Column '{column_filter}' not found in the dataset.")
        return
 
    # Plotting the specified column for each msn in the list
    plt.figure(figsize=(20, 6))
 
    for msn in msn_filters:
        msn_data = filtered_data[filtered_data['msn'] == msn]
        plt.plot(msn_data['time'], msn_data[column_filter], marker='o', linestyle='-', label=msn)
 
    plt.title(f'{column_filter} vs Time for {", ".join(msn_filters)} on {date_filter}')
    plt.xlabel('Time (hh:mm:ss)')
    plt.ylabel(column_filter)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title='MSN')
 
    plt.tight_layout()
    st.pyplot(plt)
#########################################################
col1,col2=st.columns([3, 5]) 
temp1=0
with col1:
    col11,coll22=st.columns([1,1])
    with col11:
        st.subheader('Please Select Msn Number')
        option_check1=st.checkbox('SM11065227')
        option_check2=st.checkbox('SM11066826')
        option_check3=st.checkbox('SM11101308')
        option_check4=st.checkbox('SM11150862')
        option_check5=st.checkbox('SM11150914')
        option_check6=st.checkbox('SML3000263')
        selected_msn = []
        if option_check1:
            selected_msn.append('SM11065227')
        if option_check2:
            selected_msn.append('SM11066826')
        if option_check3:
            selected_msn.append('SM11101308')
        if option_check4:
            selected_msn.append('SM11150862')
        if option_check5:
            selected_msn.append('SM11150914')
        if option_check6:
            selected_msn.append('SML3000263')
    if len(selected_msn)!=0:
        with coll22:
            temp=st.text_input("Please Enter the Date(1-30)")
            if temp:
                try:
                    temp1=int(temp)
                    while temp1< 1 or temp1>30:
                        st.write("Please Enter The Valid Date")
                        temp=st.text_input("Re-enter:",'enter')
                        temp1=int(temp)
                except ValueError:
                    st.write("Please enter a valid number.")
            st.write(f"you have selected : {temp}")
            st.write('Please Select Parameter')
            option3 = st.selectbox('',('v_ave','i_ave','wh_imp','vah_imp'))
            st.write(f"you have selected: {option3}")
    else:
        st.write("Please First Select Msn Number")
if temp1!=0:
    with col2:
        if temp1%10==temp1:
            date=f'2024-11-0{temp1}'
        else:
            date =f'2024-11-{temp1}'  # The specific date to plot

        plot_dynamic_data_multiple_msn(selected_msn, date,option3)