#
#   Copyright 2023 Hopsworks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from hsfs.core.job_scheduler import JobScheduler
from hsfs.core import feature_monitoring_config as fmc
from hsfs.core.monitoring_window_config import WindowConfigType


class TestFeatureMonitoringConfig:
    def test_from_response_json_via_fg(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"][
            "get_via_feature_group"
        ]["detection_insert_reference_snapshot"]["response"]

        # Act
        config = fmc.FeatureMonitoringConfig.from_response_json(config_json)

        # Assert
        assert config._id == 32
        assert config._feature_store_id == 67
        assert config._feature_group_id == 13
        assert config._href[-2:] == "32"
        assert config._feature_name == "monitored_feature"
        assert config._enabled is True
        assert config._name == "unit_test_config"
        assert (
            config._feature_monitoring_type
            == fmc.FeatureMonitoringType.STATISTICS_COMPARISON
        )

        assert isinstance(config._scheduler_config, JobScheduler)
        assert config._scheduler_config.id == 222
        assert config._scheduler_config.job_frequency == "DAILY"
        assert (
            config._scheduler_config.job_name
            == "fg_or_fv_name_version_fm_config_name_run_feature_monitoring"
        )
        assert config._scheduler_config.enabled is True
        assert config._scheduler_config.start_date_time == 1676457000000

        assert (
            config._detection_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._detection_window_config.time_offset == "1w"
        assert config._detection_window_config.window_length == "1d"
        assert (
            config._reference_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._reference_window_config.time_offset == "1w"

        assert config._statistics_comparison_config["threshold"] == 1
        assert config._statistics_comparison_config["strict"] is True
        assert config._statistics_comparison_config["relative"] is False
        assert config._statistics_comparison_config["metric"] == "MEAN"

    def test_from_response_json_via_fv(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"][
            "get_via_feature_view"
        ]["detection_insert_reference_snapshot"]["response"]

        # Act
        config = fmc.FeatureMonitoringConfig.from_response_json(config_json)

        # Assert
        assert config._id == 32
        assert config._feature_store_id == 67
        assert config._feature_view_id == 22
        assert config._feature_group_id is None
        assert config._href[-2:] == "32"
        assert config._feature_name == "monitored_feature"
        assert config._enabled is True
        assert config._name == "unit_test_config"
        assert (
            config._feature_monitoring_type
            == fmc.FeatureMonitoringType.STATISTICS_COMPARISON
        )

        assert isinstance(config._scheduler_config, JobScheduler)
        assert config._scheduler_config.id == 222
        assert config._scheduler_config.job_frequency == "DAILY"
        assert (
            config._scheduler_config.job_name
            == "fg_or_fv_name_version_fm_config_name_run_feature_monitoring"
        )
        assert config._scheduler_config.enabled is True
        assert config._scheduler_config.start_date_time == 1676457000000

        assert (
            config._detection_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._detection_window_config.time_offset == "1w"
        assert config._detection_window_config.window_length == "1d"
        assert (
            config._reference_window_config.window_config_type
            == WindowConfigType.TRAINING_DATASET
        )
        assert config._reference_window_config.training_dataset_id == 33

        assert config._statistics_comparison_config["threshold"] == 1
        assert config._statistics_comparison_config["strict"] is True
        assert config._statistics_comparison_config["relative"] is False
        assert config._statistics_comparison_config["metric"] == "MEAN"

    def test_from_response_json_stats_only_via_fg(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"][
            "get_via_feature_group"
        ]["detection_insert_scheduled_stats_only"]["response"]

        # Act
        config = fmc.FeatureMonitoringConfig.from_response_json(config_json)

        # Assert
        assert config._id == 32
        assert config._feature_store_id == 67
        assert config._feature_view_id is None
        assert config._feature_group_id == 13
        assert config._href[-2:] == "32"
        assert config._name == "unit_test_config"
        assert config._feature_name == "monitored_feature"
        assert config._enabled is True
        assert config._feature_monitoring_type == "STATISTICS_MONITORING"

        assert isinstance(config._scheduler_config, JobScheduler)
        assert config._scheduler_config.id == 222
        assert config._scheduler_config.job_frequency == "HOURLY"
        assert (
            config._scheduler_config.job_name
            == "fg_or_fv_name_version_fm_config_name_run_feature_monitoring"
        )
        assert config._scheduler_config.enabled is False
        assert config._scheduler_config.start_date_time == 1676457000000

        assert (
            config._detection_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._detection_window_config.time_offset == "1w"
        assert config._detection_window_config.window_length == "1d"

    def test_from_response_json_stats_only_via_fv(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"][
            "get_via_feature_view"
        ]["detection_insert_scheduled_stats_only"]["response"]

        # Act
        config = fmc.FeatureMonitoringConfig.from_response_json(config_json)

        # Assert
        assert config._id == 32
        assert config._feature_store_id == 67
        assert config._feature_view_id == 22
        assert config._feature_group_id is None
        assert config._href[-2:] == "32"
        assert config._name == "unit_test_config"
        assert config._feature_name == "monitored_feature"
        assert config._enabled is True
        assert config._feature_monitoring_type == "STATISTICS_MONITORING"

        assert isinstance(config._scheduler_config, JobScheduler)
        assert config._scheduler_config.id == 222
        assert config._scheduler_config.job_frequency == "HOURLY"
        assert (
            config._scheduler_config.job_name
            == "fg_or_fv_name_version_fm_config_name_run_feature_monitoring"
        )
        assert config._scheduler_config.enabled is False
        assert config._scheduler_config.start_date_time == 1676457000000

        assert (
            config._detection_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._detection_window_config.time_offset == "1w"
        assert config._detection_window_config.window_length == "1d"

    def test_from_response_json_list(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"]["get_list"][
            "response"
        ]

        # Act
        config_list = fmc.FeatureMonitoringConfig.from_response_json(config_json)
        config = config_list[0]

        # Assert
        assert isinstance(config_list, list)
        assert len(config_list) == 1
        assert isinstance(config, fmc.FeatureMonitoringConfig)
        assert config._id == 32
        assert config._feature_store_id == 67
        assert config._feature_view_id == 22
        assert config._feature_group_id is None
        assert config._href[-2:] == "32"
        assert config._feature_name == "monitored_feature"
        assert config._enabled is True
        assert (
            config._feature_monitoring_type
            == fmc.FeatureMonitoringType.STATISTICS_COMPARISON
        )

        assert isinstance(config._scheduler_config, JobScheduler)
        assert config._scheduler_config.id == 222
        assert config._scheduler_config.job_frequency == "HOURLY"
        assert (
            config._scheduler_config.job_name
            == "fg_or_fv_name_version_fm_config_name_run_feature_monitoring"
        )
        assert config._scheduler_config.enabled is False
        assert config._scheduler_config.start_date_time == 1676457000000

        assert (
            config._detection_window_config.window_config_type
            == WindowConfigType.ROLLING_TIME
        )
        assert config._detection_window_config.time_offset == "1w"
        assert config._detection_window_config.window_length == "1d"
        assert (
            config._reference_window_config.window_config_type
            == WindowConfigType.TRAINING_DATASET
        )
        assert config._reference_window_config.training_dataset_id == 33

        assert config._statistics_comparison_config["threshold"] == 1
        assert config._statistics_comparison_config["strict"] is True
        assert config._statistics_comparison_config["relative"] is False
        assert config._statistics_comparison_config["metric"] == "MEAN"

    def test_from_response_json_list_empty(self, backend_fixtures):
        # Arrange
        config_json = backend_fixtures["feature_monitoring_config"]["get_list_empty"][
            "response"
        ]

        # Act
        config_list = fmc.FeatureMonitoringConfig.from_response_json(config_json)

        # Assert
        assert isinstance(config_list, list)
        assert len(config_list) == 0