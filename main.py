from frontend import app
import dutch_statistics as dutch
import graph_plotter
import datetime


def refresh_dutch_statistics():
    dutch.get_dutch_stats()
    dutch.calculate_dutch_daily_statistics()


def quick_caller(municipality=None, province=None):
    return graph_plotter.plot_statistics(
            data_set=dutch.sum_dutch_total_infections(municipality=municipality, province=province),
            start_date=datetime.date(2020, 7, 6),
            no_days_to_predict=7,
            linear_regres=True,
            exp_curve=True)
