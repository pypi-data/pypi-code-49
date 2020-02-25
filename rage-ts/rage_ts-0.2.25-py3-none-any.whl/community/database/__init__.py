# this file imports all SQL tables at module level - this avoids
# reference to non-existing tables in SQL relations

# noinspection PyUnresolvedReferences
from ragex.community.database.admin import (
    Project,
    User,
    PlatformFeature,
    Role,
    Environment,
    Permission,
    ChatToken,
    LocalPassword,
    SingleUseToken,
    ConfigValue,
    GitRepository,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.conversation import (
    Conversation,
    ConversationActionMetadata,
    ConversationEntityMetadata,
    ConversationEvent,
    ConversationIntentMetadata,
    ConversationMessageCorrection,
    ConversationPolicyMetadata,
    MessageLog,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.analytics import (
    ConversationActionStatistic,
    ConversationEntityStatistic,
    ConversationIntentStatistic,
    ConversationPolicyStatistic,
    ConversationStatistic,
    ConversationSession,
    AnalyticsCache,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.data import (
    TrainingData,
    Template,
    Story,
    EntitySynonymValue,
    EntitySynonym,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.domain import (
    Domain,
    DomainAction,
    DomainEntity,
    DomainIntent,
    DomainSlot,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.intent import (
    Intent,
    UserGoal,
    TemporaryIntentExample,
    UserGoalIntent,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.model import (
    Model,
    ModelTag,
    NluEvaluation,
    NluEvaluationPrediction,
)

# noinspection PyUnresolvedReferences
from ragex.community.database.response import (
    IntentResTemplate
)