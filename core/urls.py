from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views.comment_views import CommentViewSet

from .views.auth_views import RegisterView

from .views.item_views import (
    LostItemListCreateView,
    LostItemDetailView,
    FoundItemListCreateView,
)

from .views.claim_views import (
    ClaimRequestCreateView,
    ApproveClaimView,
    RejectClaimView,
)

from .views.match_views import FoundItemMatchView
from .views.history_views import MatchHistoryListView
from .views.notification_views import NotificationListView

# ✅ DRF ROUTER
router = DefaultRouter()
router.register(r"comments", CommentViewSet, basename="comments")


urlpatterns = [

    # 🔐 AUTH
    path("register/", RegisterView.as_view()),

    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),


    # 📦 ITEMS
    path("lost-items/", LostItemListCreateView.as_view()),
    path("lost-items/<int:pk>/", LostItemDetailView.as_view()),

    path("found-items/", FoundItemListCreateView.as_view()),


    # 🔗 CLAIMS
    path("claims/", ClaimRequestCreateView.as_view()),

    path("claims/<int:pk>/approve/", ApproveClaimView.as_view()),
    path("claims/<int:pk>/reject/", RejectClaimView.as_view()),


    # 🤖 MATCHING
    path(
        "found-items/<int:pk>/matches/",
        FoundItemMatchView.as_view()
    ),


    # 📊 HISTORY
    path(
        "match-history/",
        MatchHistoryListView.as_view()
    ),


    # 💬 COMMENTS ROUTER
    path("", include(router.urls)),
    path(
    "notifications/",
    NotificationListView.as_view()
),
]