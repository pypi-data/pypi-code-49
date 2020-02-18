from zalando_kubectl.models.bluegreen import BlueGreen


class IngressTemplate(BlueGreen):
    def __init__(self, ingress_def):
        super().__init__(ingress_def)

        for rule in self.definition["spec"].get("rules", []):
            for path in rule.get("http", {}).get("paths", []):
                if path.get("backend"):
                    # Negative number means there is no desired traffic
                    self.stacks[path["backend"]["serviceName"]] = -1

    def get_stacks_to_update(self):
        return self.stacks_status

    def get_all_stacks(self):
        return self.stacks

    def validate_traffic_weight(self, stack_name: str, weight: float):
        if stack_name not in self.stacks:
            raise ValueError("Backend {} does not exist.".format(stack_name))

        if len(self.stacks) == 1 and weight not in (0, 100):
            raise ValueError("Backend {} is the only one; weight must be either 0 or 100.".format(stack_name))

        if self.get_traffic_complement(stack_name) == 0 and len(self.stacks) != 1:
            raise ValueError(
                "All stacks other than {} have no weight. Please choose a different one.".format(stack_name)
            )
