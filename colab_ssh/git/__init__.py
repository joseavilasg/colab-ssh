
from .github import github_provider
providers = {
    "github": github_provider,
}


__all__ = [
    "providers"
]
