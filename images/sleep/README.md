Sleep task
--
[![](https://images.microbadger.com/badges/image/als23/sleep.svg)](https://microbadger.com/images/als23/sleep "Get your own image badge on microbadger.com")

1. Embarrassingly parallel problem;
2. To build an image use `docker build -t sleep .`;
3. To run it use `docker run sleep python3 run.py 100 50`,
if you'd like to run simulation of 100 secs sleep on 50 CPUs;
4. Computation time will be calculated by completion.
