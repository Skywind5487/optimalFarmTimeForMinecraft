import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson
from scipy.optimize import minimize_scalar


class rate_calculator:
    def __init__(
            self, 
            binomial_func,
            poisson_func=None,
            max_ticks=10**6, 
            p=1/40960,
            title="Growth Rate Analysis",
            rate=10**2,
            search_range=100):
        """Initialize rate calculator with parameters
        
        Args:
            binomial_func: Function to calculate binomial rate
            poisson_func: Function to calculate poisson rate (optional)
            max_ticks (int): Maximum number of ticks to consider
            p (float): Probability of success per tick
            title (str): Title for the plot
        """
        self.max_ticks = int(max_ticks)
        self.p = p
        self.title = title
        self.binomial_func = binomial_func
        self.poisson_func = poisson_func
        
        # Generate x values for plotting
        self.x_values = np.linspace(1, max_ticks, max_ticks//rate)
        
        # Calculate maximum points
        self._calculate_maximum_points(search_range=search_range)

        # Create the plot
        self.fig = None
    
    def _calculate_maximum_points(self, search_range=100):
        """Calculate maximum points for both distributions"""
        # Calculate rates for binomial distribution
        self.binomial_rates = [self.binomial_func(x, self.p) for x in self.x_values]
        self.max_bin_x, self.max_bin_rate = self._find_max_rate_point(
            lambda x: self.binomial_func(x, self.p),
            search_range=search_range
        )
        self.bin_time_str = self.convert_ticks(self.max_bin_x)

        # Initialize poisson attributes to None
        self.poisson_rates = None
        self.max_poi_x = None
        self.max_poi_rate = None
        self.poi_time_str = None

        # Calculate rates for Poisson distribution if function provided
        if self.poisson_func is not None:
            self.poisson_rates = [self.poisson_func(x, self.p) for x in self.x_values]
            self.max_poi_x, self.max_poi_rate = self._find_max_rate_point(
                lambda x: self.poisson_func(x, self.p),
                search_range=search_range
            )
            self.poi_time_str = self.convert_ticks(self.max_poi_x)

    def _find_max_rate_point(self, rate_func, search_range):
        """Find maximum rate point using minimize_scalar"""
        def negative_rate(x):
            return -rate_func(x)
        
        result = minimize_scalar(
            negative_rate, 
            bounds=(1, self.max_ticks),
            method='bounded'
        )
        
        x_max_approx = result.x
        search_range = search_range
        x_nearby = np.arange(
            max(int(x_max_approx - search_range), 1),
            min(int(x_max_approx + search_range ), self.max_ticks)
        )
        rates_nearby = [rate_func(x) for x in x_nearby]
        max_idx = np.argmax(rates_nearby)
        
        return x_nearby[max_idx], rates_nearby[max_idx]

    def convert_ticks(self, ticks:int) -> str:
        """Convert ticks to readable time format"""
        total_ticks = ticks
        total_seconds = ticks / 20
        ticks = int(ticks % 20)
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        
        time_parts = []
        if hours > 0:
            time_parts.append(f"{hours}h")
        if minutes > 0:
            time_parts.append(f"{minutes}m")
        if seconds > 0 or ticks > 0:
            time_parts.append(f"{seconds}s")
        if ticks > 0:
            time_parts.append(f"{ticks}tick")
        time_str = " ".join(time_parts)
        return f"{time_str}, aka {int(total_ticks)} ticks"

    def convert_rate(self, rate:int) -> str:
        """Convert rate from items/tick to items/hour
        
        Args:
            rate (float): Rate in items per tick
        
        Returns:
            str: Formatted string with hourly rate
        """
        hourly_rate = rate * 20 * 60 * 60  # Convert to items per hour
        if hourly_rate > 1e6:
            return f"{hourly_rate / 1e6:.10f}M/hour"
        elif hourly_rate > 1e3:
            return f"{hourly_rate / 1e3:.10f}K/hour"
        else:
            return f"{hourly_rate:.10f}/hour"

    def show(self):
        """Display calculation results with hourly rates"""
        print("===== Results Output =====")
        print(f"[Binomial]")
        print(f"Maximum rate(per tick): {self.max_bin_rate:.20f}")
        print(f"Maximum rate(per hour): {self.convert_rate(self.max_bin_rate)}")
        print(f"Time: {self.bin_time_str}")
        
        if self.poisson_func is not None and self.max_poi_rate is not None:
            print(f"\n[Poisson]")
            print(f"Maximum rate(per tick): {self.max_poi_rate:.20f}")
            print(f"Maximum rate: {self.convert_rate(self.max_poi_rate)}")
            print(f"Time: {self.poi_time_str}")    
    def _create_plot(self):
        """Create the rate comparison plot and return the figure"""
        # Configure font settings for Chinese support
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
        plt.rcParams['axes.unicode_minus'] = True

        fig = plt.figure(figsize=(10, 6))
        plt.subplots_adjust(hspace=0.5)
        
        # Convert rates to hourly rates for plotting
        hourly_bin_rates = [rate * 20 * 60 * 60 for rate in self.binomial_rates]
        plt.plot(self.x_values, hourly_bin_rates, 
                label='Binomial Distribution', color='blue')
        
        # Mark maximum points for binomial
        hourly_bin_rate = self.max_bin_rate * 20 * 60 * 60
        plt.scatter(self.max_bin_x, hourly_bin_rate, color='blue', zorder=5)
        
        # Add binomial label with offset
        y_offset = (plt.ylim()[1] - plt.ylim()[0]) * 0.02
        plt.text(self.max_bin_x, hourly_bin_rate - y_offset, 
                f'Bin Max\n({int(self.max_bin_x)}, {self.convert_rate(self.max_bin_rate)})', 
                fontsize=9, ha='right', va='top', color='blue')

        # Plot Poisson if available
        if self.poisson_func is not None and self.poisson_rates is not None:
            hourly_poi_rates = [rate * 20 * 60 * 60 for rate in self.poisson_rates]
            plt.plot(self.x_values, hourly_poi_rates, 
                    label='Poisson Distribution', color='green')
            
            hourly_poi_rate = self.max_poi_rate * 20 * 60 * 60
            plt.scatter(self.max_poi_x, hourly_poi_rate, color='green', zorder=5)
            
            plt.text(self.max_poi_x, hourly_poi_rate - 10*y_offset, 
                    f'Poi Max\n({int(self.max_poi_x)}, {self.convert_rate(self.max_poi_rate)})', 
                    fontsize=9, ha='right', va='top', color='green')

        plt.xlabel("Time (ticks)")
        plt.ylabel("Rate (Items / hour)")
        plt.title(self.title)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        
        return fig

    def plot(self, save_path=None):
        """Display and optionally save the rate comparison plot
        
        Args:
            save_path (str, optional): If provided, save the plot to this path
        """

        if not self.fig:
            self.fig = self._create_plot()
            fig = self.fig
        else:
            fig = self.fig

        if save_path:
            fig.savefig(save_path)
            print(f"Plot saved as {save_path}")

        plt.show()
        plt.close(fig)
    
    def save_plot(self, filename):
        """Save the plot to a file without displaying it
        
        Args:
            filename (str): Path where to save the plot
        """
        if not self.fig:
            self.fig = self._create_plot()
            fig = self.fig
        else:
            fig = self.fig
        fig.savefig(filename)
        plt.close(fig)
        print(f"Plot saved as {filename}")
