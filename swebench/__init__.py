__version__ = "3.0.15"

# Removed references to collect module which we don't need for evaluation

from swebench.harness.constants import (
    KEY_INSTANCE_ID,
    KEY_MODEL,
    KEY_PREDICTION,
    MAP_REPO_VERSION_TO_SPECS,
)

from swebench.harness.docker_build import (
    build_image,
    build_base_images,
    build_env_images,
    build_instance_images,
    build_instance_image,
    close_logger,
    setup_logger,
)

from swebench.harness.docker_utils import (
    cleanup_container,
    remove_image,
    copy_to_container,
    exec_run_with_timeout,
    list_images,
)

from swebench.harness.grading import (
    compute_fail_to_pass,
    compute_pass_to_pass,
    get_logs_eval,
    get_eval_report,
    get_resolution_status,
    ResolvedStatus,
    TestStatus,
)

from swebench.harness.log_parsers import (
    MAP_REPO_TO_PARSER,
)

from swebench.harness.run_evaluation import (
    run_instances,  # Export run_instances directly
    main as run_evaluation,
    clean_images,  # Import clean_images from run_evaluation
)

from swebench.harness.utils import (
    run_threadpool,
    load_swebench_dataset,
    EvaluationError,
)
