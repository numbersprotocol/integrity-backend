import pytest

from .context import config
from .context import asset_helper


def test_rejects_non_file_safe_org():
    with pytest.raises(ValueError, match="filename safe"):
        asset_helper.AssetHelper("not File Safe")


def test_directory_contains_org():
    helper = asset_helper.AssetHelper("example")
    assert helper.get_claims_internal() == "/tests/assets_dir/example/claims"

def test_create_output_contains_subfolders(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "SHARED_FILE_SYSTEM", tmp_path / "shared_dir")

    helper = asset_helper.AssetHelper("example")
    assert helper.get_assets_create_output(["Jane Doe", "2022-02-17"]).endswith(
        "/shared_dir/example/create-output/jane-doe/2022-02-17"
    )

def test_create_output_works_without_subfolders(monkeypatch, tmp_path):
    monkeypatch.setattr(config, "SHARED_FILE_SYSTEM", tmp_path / "shared_dir")

    helper = asset_helper.AssetHelper("example")
    assert helper.get_assets_create_output().endswith("/shared_dir/example/create-output")
