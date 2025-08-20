# main.py
import medical_data_visualizer as mdv

def main():
    print("Loading medical examination data...")
    csv_file = "medical_examination.csv"
    data = mdv.load_data(csv_file)
    print(f"Data loaded: {data.shape[0]} rows, {data.shape[1]} columns\n")

    print("Generating categorical plot...")
    cat_fig = mdv.draw_cat_plot(data)
    print("Categorical plot created.")
    cat_fig.show()

    print("\nGenerating heat map...")
    heat_fig = mdv.draw_heat_map(data)
    print("Heat map created.")
    heat_fig.show()

    print("\nAll plots generated successfully!")
    plt.show()

if __name__ == "__main__":
    main()
