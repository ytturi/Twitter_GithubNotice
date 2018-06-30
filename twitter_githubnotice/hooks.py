from hookshub.hook import Hook
from hookshub.parser import HookParser
from hookshub.hooks.github import GitHubUtil
from hookshub.hooks.gitlab import GitLabUtil


def twitter_notify(args):
    confs = args['conf']
    event = args['event']
    action = args['action']
    origin = args['origin']
    print('Running Hook for {} from {}'.format(event, origin))


def twitter_hooks_args(payload, confs):
    dict = {}
    webhook = HookParser.instancer(payload=payload)
    if conf:
        dict['conf'] = conf
    dict['event'] = webhook.event
    dict['origin'] = webhook.origin
    dict['action'] = webhook.action if webhook.origin == 'github' else False
    return dict


class GHMergeHook(Hook):
    def __init__(self):
        super(GHMergeHook, self).__init__(
            method=twitter_notify,
            event=GitHubUtil.events['EVENT_PULL_REQUEST'],
            repository=False,
            branch=False
        )

    def get_args(self, webhook=False, conf=False):
        return twitter_hooks_args(payload=webhook, confs=conf)


class GHMPushHook(Hook):
    def __init__(self):
        super(GHMPushHook, self).__init__(
            method=twitter_notify,
            event=GitHubUtil.events['EVENT_PULL_REQUEST'],
            repository=False,
            branch=False
        )

    def get_args(self, webhook=False, conf=False):
        return twitter_hooks_args(payload=webhook, confs=conf)


class GLMergeHook(Hook):
    def __init__(self):
        super(GLMergeHook, self).__init__(
            method=twitter_notify,
            event=GitLabUtil.events['EVENT_MERGE_REQ'],
            repository=False,
            branch=False
        )

    def get_args(self, webhook=False, conf=False):
        return twitter_hooks_args(payload=webhook, confs=conf)


class GLMPushHook(Hook):
    def __init__(self):
        super(GLMPushHook, self).__init__(
            method=twitter_notify,
            event=GitLabUtil.events['EVENT_PUSH'],
            repository=False,
            branch=False
        )

    def get_args(self, webhook=False, conf=False):
        return twitter_hooks_args(payload=webhook, confs=conf)