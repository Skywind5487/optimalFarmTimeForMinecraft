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
            title="Growth Rate Analysis"):
        """Initialize rate calculator with parameters
        
        Args:
            binomial_func: Function to calculate binomial yield
            poisson_func: Function to calculate poisson yield (optional)
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
        self.x_values = np.linspace(1, max_ticks, max_ticks//10**2)
        
        # Calculate maximum points
        self._calculate_maximum_points()
    
    def _calculate_maximum_points(self):
        """Calculate maximum points for both distributions"""
        # Calculate rates for binomial distribution
        self.binomial_rates = [self.binomial_func(x, self.p) for x in self.x_values]
        self.max_bin_x, self.max_bin_yield = self._find_max_rate_point(
            lambda x: self.binomial_func(x, self.p)
        )
        self.bin_time_str = self._convert_ticks(self.max_bin_x)

        # Initialize poisson attributes to None
        self.poisson_rates = None
        self.max_poi_x = None
        self.max_poi_yield = None
        self.poi_time_str = None

        # Calculate rates for Poisson distribution if function provided
        if self.poisson_func is not None:
            self.poisson_rates = [self.poisson_func(x, self.p) for x in self.x_values]
            self.max_poi_x, self.max_poi_yield = self._find_max_rate_point(
                lambda x: self.poisson_func(x, self.p)
            )
            self.poi_time_str = self._convert_ticks(self.max_poi_x)

    def _find_max_rate_point(self, rate_func):
        """Find maximum rate point using minimize_scalar"""
        def negative_rate(x):
            return -rate_func(x)
        
        result = minimize_scalar(
            negative_rate, 
            bounds=(0, self.max_ticks),
            method='bounded'
        )
        
        x_max_approx = result.x
        search_range = 100
        x_nearby = np.arange(
            int(x_max_approx - search_range), 
            int(x_max_approx + search_range + 1)
        )
        rates_nearby = [rate_func(x) for x in x_nearby]
        max_idx = np.argmax(rates_nearby)
        
        return x_nearby[max_idx], rates_nearby[max_idx]

    def _convert_ticks(self, ticks):
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

    def _convert_rate(self, rate):
        """Convert rate from items/tick to items/hour
        
        Args:
            rate (float): Rate in items per tick
        
        Returns:
            str: Formatted string with hourly rate
        """
        hourly_rate = rate * 20 * 60 * 60  # Convert to items per hour
        if hourly_rate > 1e6:
            return f"{hourly_rate / 1e6:.3f}M/hour"
        elif hourly_rate > 1e3:
            return f"{hourly_rate / 1e3:.3f}K/hour"
        else:
            return f"{hourly_rate:.3f}/hour"

    def show(self):
        """Display calculation results with hourly rates"""
        print("===== Results Output =====")
        print(f"[Binomial]")
        print(f"Maximum rate(per tick): {self.max_bin_yield:.20f}")
        print(f"Maximum rate(per hour): {self._convert_rate(self.max_bin_yield)}")
        print(f"Time: {self.bin_time_str}")
        
        if self.poisson_func is not None and self.max_poi_yield is not None:
            print(f"\n[Poisson]")
            print(f"Maximum rate(per tick): {self.max_poi_yield:.20f}")
            print(f"Maximum rate: {self._convert_rate(self.max_poi_yield)}")
            print(f"Time: {self.poi_time_str}")

    def plot(self):
        """Plot the rate comparison graph"""
        # Configure font settings for Chinese support
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
        plt.rcParams['axes.unicode_minus'] = True

        plt.figure(figsize=(10, 6))
        plt.subplots_adjust(hspace=0.5)
        
        # Convert rates to hourly rates for plotting
        hourly_bin_rates = [rate * 20 * 60 * 60 for rate in self.binomial_rates]
        plt.plot(self.x_values, hourly_bin_rates, 
                label='Binomial Distribution', color='blue')
        
        # Mark maximum points for binomial
        hourly_bin_yield = self.max_bin_yield * 20 * 60 * 60
        plt.scatter(self.max_bin_x, hourly_bin_yield, color='blue', zorder=5)
        
        # Add binomial label with offset
        y_offset = (plt.ylim()[1] - plt.ylim()[0]) * 0.02
        plt.text(self.max_bin_x, hourly_bin_yield - y_offset, 
                f'Bin Max\n({int(self.max_bin_x)}, {self._convert_rate(self.max_bin_yield)})', 
                fontsize=9, ha='right', va='top', color='blue')

        # Plot Poisson if available
        if self.poisson_func is not None and self.poisson_rates is not None:
            hourly_poi_rates = [rate * 20 * 60 * 60 for rate in self.poisson_rates]
            plt.plot(self.x_values, hourly_poi_rates, 
                    label='Poisson Distribution', color='green')
            
            hourly_poi_yield = self.max_poi_yield * 20 * 60 * 60
            plt.scatter(self.max_poi_x, hourly_poi_yield, color='green', zorder=5)
            
            plt.text(self.max_poi_x, hourly_poi_yield - 10*y_offset, 
                    f'Poi Max\n({int(self.max_poi_x)}, {self._convert_rate(self.max_poi_yield)})', 
                    fontsize=9, ha='right', va='top', color='green')

        plt.xlabel("Time (ticks)")
        plt.ylabel("Rate (Items / hour)")
        plt.title(self.title)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
