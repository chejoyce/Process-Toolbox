def main():
    st.title("Excel Data Visualizer")

    # Button to browse an Excel file
    excel_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if excel_file is not None:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(excel_file)

        if st.checkbox("Show Excel Data"):
            st.write(df)

        if st.button("Visualize Data"):
            # Visualize the data as 4 bar graphs
            st.subheader("Bar Graphs")
            for column in df.columns:
                if df[column].dtype == "int64" or df[column].dtype == "float64":
                    fig, ax = plt.subplots()
                    ax.bar(df.index, df[column])
                    ax.set_xlabel("Index")
                    ax.set_ylabel(column)
                    st.pyplot(fig)

if __name__ == "__main__":
    main()
