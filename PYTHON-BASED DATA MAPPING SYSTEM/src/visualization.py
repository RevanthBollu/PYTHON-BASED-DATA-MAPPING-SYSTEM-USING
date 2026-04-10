from bokeh.plotting import figure, show, output_file

class Visualizer:

    def plot(self, train, ideal, results):

        output_file("visualization.html")

        p = figure(
            title="Function Mapping",
            width=800,
            height=600,
            x_axis_label="X",
            y_axis_label="Y"
        )

        # training data
        p.scatter(
            train["x"],
            train["y1"],
            size=6,
            color="blue",
            legend_label="Training Data"
        )

        # ideal function
        p.line(
            ideal["x"],
            ideal["y1"],
            line_width=2,
            color="green",
            legend_label="Ideal Function"
        )

        # test mapped points
        if not results.empty:
            p.scatter(
                results["x"],
                results["y"],
                size=6,
                color="red",
                legend_label="Mapped Test Data"
            )

        show(p)