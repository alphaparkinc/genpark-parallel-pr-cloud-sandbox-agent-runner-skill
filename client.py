class ParallelPrCloudSandboxAgentRunnerClient:
    def provision_sandboxes(self, pr_list: list = None, sandbox_region: str = "us-east-1") -> dict:
        pr_list = pr_list or ["PR#401 - auth-refactor", "PR#402 - db-migration", "PR#403 - ui-redesign"]
        instances = [
            {"pr": pr, "sandbox_id": f"sbx-{i+1:04d}", "region": sandbox_region, "status": "RUNNING", "agent": "claude-code-agent-v3"}
            for i, pr in enumerate(pr_list)
        ]
        return {
            "sandbox_instances": instances,
            "total_parallel_agents": len(pr_list),
            "estimated_completion_minutes": len(pr_list) * 4.5
        }
