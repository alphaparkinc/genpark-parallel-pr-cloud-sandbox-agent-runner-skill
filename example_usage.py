from client import ParallelPrCloudSandboxAgentRunnerClient

def main():
    client = ParallelPrCloudSandboxAgentRunnerClient()
    prs = ["PR#501 - payment-service", "PR#502 - search-index", "PR#503 - notification-engine"]
    res = client.provision_sandboxes(prs, "eu-west-1")
    print(f"Total Parallel Agents: {res['total_parallel_agents']}")
    print(f"Est. Completion: {res['estimated_completion_minutes']} min")
    for inst in res["sandbox_instances"]:
        print(f"  [{inst['sandbox_id']}] {inst['pr']} -> {inst['status']} ({inst['agent']})")

if __name__ == "__main__":
    main()
