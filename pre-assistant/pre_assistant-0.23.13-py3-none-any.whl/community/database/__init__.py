# NOTE: If you add / remove / change SQLAlchemy models you have to add a schema
# migration. Please see the readme how to do so.

# this file imports all SQL tables at module level - this avoids
# reference to non-existing tables in SQL relations

# noinspection PyUnresolvedReferences
from rasax.community.database.admin import (
    Project,
    User,
    PlatformFeature,
    Role,
    Environment,
    Permission,
    ChatToken,
    LocalPassword,
    SingleUseToken,
)

# noinspection PyUnresolvedReferences
from rasax.community.database.conversation import (
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
from rasax.community.database.analytics import (
    ConversationActionStatistic,
    ConversationEntityStatistic,
    ConversationIntentStatistic,
    ConversationPolicyStatistic,
    ConversationStatistic,
    ConversationSession,
    AnalyticsCache,
)

# noinspection PyUnresolvedReferences
from rasax.community.database.data import TrainingData, Template, Story

# noinspection PyUnresolvedReferences
from rasax.community.database.domain import (
    Domain,
    DomainAction,
    DomainEntity,
    DomainIntent,
    DomainSlot,
)

# noinspection PyUnresolvedReferences
from rasax.community.database.intent import (
    Intent,
    UserGoal,
    TemporaryIntentExample,
    UserGoalIntent,
)

# noinspection PyUnresolvedReferences
from rasax.community.database.model import (
    Model,
    ModelTag,
    NluEvaluation,
    NluEvaluationPrediction,
)
