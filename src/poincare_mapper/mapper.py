from scipy.integrate import solve_ivp


class PoincareMapper:
    def __init__(self, system, section):
        self.system = system
        self.section = section

    def run(
        self,
        initial_state,
        t_span=(0, 1000),
        rtol=1e-9,
        atol=1e-12,
        burn_in=0,
        max_step=0.05,
    ):
        sol = solve_ivp(
            self.system,
            t_span,
            initial_state,
            events=self.section,
            rtol=rtol,
            atol=atol,
            max_step=max_step,
        )

        crossings = sol.y_events[0]
        times = sol.t_events[0]

        if crossings.size == 0:
            crossings = crossings.reshape(0, len(initial_state))

        if burn_in > 0:
            crossings = crossings[burn_in:]
            times = times[burn_in:]

        return {
            "crossings": crossings,
            "times": times,
        }
