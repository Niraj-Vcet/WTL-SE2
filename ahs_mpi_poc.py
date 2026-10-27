from mpi4py import MPI
import time
import math


# ---------------------------------------
# AHS-like simulation workload
# ---------------------------------------
def run_simulation(workload_id):
    """
    Simple computational workload representing
    an independent AHS simulation.

    This is NOT a real AHS simulator yet.
    """

    start = time.perf_counter()

    result = 0.0

    # Simulate computational work
    for i in range(1, 2_000_000):
        result += math.sin(i * 0.0001) ** 2

    execution_time = time.perf_counter() - start

    return {
        "workload_id": workload_id,
        "result": result,
        "time": execution_time
    }


# ---------------------------------------
# MPI initialization
# ---------------------------------------
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()


# ---------------------------------------
# AHS workloads
# ---------------------------------------
workloads = list(range(8))


# ---------------------------------------
# Start total execution timer
# ---------------------------------------
comm.Barrier()

total_start = MPI.Wtime()


# ---------------------------------------
# Divide workloads among MPI ranks
# ---------------------------------------
my_workloads = workloads[rank::size]


print(
    f"Rank {rank}: assigned workloads {my_workloads}"
)


# ---------------------------------------
# Execute simulations
# ---------------------------------------
local_results = []

for workload in my_workloads:

    result = run_simulation(workload)

    local_results.append(result)


# ---------------------------------------
# Gather results at Rank 0
# ---------------------------------------
all_results = comm.gather(local_results, root=0)


# ---------------------------------------
# End total execution timer
# ---------------------------------------
comm.Barrier()

total_time = MPI.Wtime() - total_start


# ---------------------------------------
# Rank 0 displays results
# ---------------------------------------
if rank == 0:

    print("\n==============================")
    print(" MPI AHS PROOF OF CONCEPT")
    print("==============================")

    print(f"Number of MPI ranks: {size}")

    print("\nSimulation Results:")

    for rank_results in all_results:

        for result in rank_results:

            print(
                f"Workload {result['workload_id']} "
                f"| Simulation time: "
                f"{result['time']:.4f} sec"
            )

    print("\n------------------------------")
    print(f"Total execution time: {total_time:.4f} sec")
    print("------------------------------")