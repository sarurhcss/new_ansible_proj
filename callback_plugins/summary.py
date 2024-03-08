import json

from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C  # NOQA


class CallbackModule(CallbackModule):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'summary'

    # This avoids errors caused by weird Ansible options handling
    def v2_runner_on_start(self, host, task):
        pass

    def v2_playbook_on_stats(self, stats):
        hosts = sorted(stats.processed.keys())
        summary = {}
        for h in hosts:
            t = stats.summarize(h)
            summary[h] = t

        with open('summary.json', 'w') as fd:
            json.dump(summary, fd, indent=2)

        super(CallbackModule, self).v2_playbook_on_stats(stats)
