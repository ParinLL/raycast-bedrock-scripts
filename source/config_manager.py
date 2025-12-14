"""
Configuration Manager for Claude Sonnet Upgrade Testing

Provides centralized configuration management for model IDs, parameters, and validation.
"""

from typing import Dict, Any, Optional
import re


class ConfigManager:
    """Centralized configuration management for Claude model settings."""
    
    # Latest APAC Claude Sonnet 4 model ID
    DEFAULT_MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
    DEFAULT_REGION = "ap-northeast-1"
    
    # Valid model ID patterns
    VALID_MODEL_PATTERNS = [
        r"anthropic\.claude-3-5-sonnet-\d{8}-v\d+:\d+",
        r"anthropic\.claude-sonnet-4-5-\d{8}-v\d+:\d+",
        r"global\.anthropic\.claude-sonnet-4-5-\d{8}-v\d+:\d+"
    ]
    
    # Valid AWS regions for Claude models
    VALID_REGIONS = [
        "us-east-1", "us-west-2", "ap-northeast-1", "ap-southeast-1", 
        "ap-southeast-2", "eu-west-1", "eu-central-1"
    ]
    
    def __init__(self, model_id: Optional[str] = None, region: Optional[str] = None):
        """
        Initialize ConfigManager with optional custom settings.
        
        Args:
            model_id: Custom model ID to use (defaults to latest APAC Claude Sonnet 4)
            region: AWS region to use (defaults to ap-northeast-1)
        """
        self._model_id = model_id or self.DEFAULT_MODEL_ID
        self._region = region or self.DEFAULT_REGION
        
        # Validate configuration on initialization
        if not self.validate_model_id(self._model_id):
            raise ValueError(f"Invalid model ID: {self._model_id}")
        if not self.validate_region(self._region):
            raise ValueError(f"Invalid region: {self._region}")
    
    def get_default_model_id(self) -> str:
        """Get the configured model ID."""
        return self._model_id
    
    def get_latest_model_id(self) -> str:
        """Get the latest available APAC Claude Sonnet 4 model ID."""
        return self.DEFAULT_MODEL_ID
    
    def get_region(self) -> str:
        """Get the configured AWS region."""
        return self._region
    
    def get_model_parameters(self) -> Dict[str, Any]:
        """
        Get default model parameters for API calls.
        
        Returns:
            Dictionary containing default parameters for model invocation
        """
        return {
            "max_tokens": 4096,
            "temperature": 1.0,
            "anthropic_version": "bedrock-2023-05-31"
        }
    
    def validate_model_id(self, model_id: str) -> bool:
        """
        Validate that a model ID follows expected patterns.
        
        Args:
            model_id: The model ID to validate
            
        Returns:
            True if model ID is valid, False otherwise
        """
        if not isinstance(model_id, str) or not model_id.strip():
            return False
            
        return any(re.match(pattern, model_id) for pattern in self.VALID_MODEL_PATTERNS)
    
    def validate_region(self, region: str) -> bool:
        """
        Validate that an AWS region is supported for Claude models.
        
        Args:
            region: The AWS region to validate
            
        Returns:
            True if region is valid, False otherwise
        """
        if not isinstance(region, str) or not region.strip():
            return False
            
        return region in self.VALID_REGIONS
    
    def validate_configuration(self) -> bool:
        """
        Validate the current configuration settings.
        
        Returns:
            True if all configuration is valid, False otherwise
        """
        return (self.validate_model_id(self._model_id) and 
                self.validate_region(self._region))
    
    def update_model_id(self, model_id: str) -> None:
        """
        Update the model ID with validation.
        
        Args:
            model_id: New model ID to use
            
        Raises:
            ValueError: If model ID is invalid
        """
        if not self.validate_model_id(model_id):
            raise ValueError(f"Invalid model ID: {model_id}")
        self._model_id = model_id
    
    def update_region(self, region: str) -> None:
        """
        Update the AWS region with validation.
        
        Args:
            region: New region to use
            
        Raises:
            ValueError: If region is invalid
        """
        if not self.validate_region(region):
            raise ValueError(f"Invalid region: {region}")
        self._region = region
    
    def get_anthropic_client_config(self) -> Dict[str, str]:
        """
        Get configuration dictionary for AnthropicBedrock client.
        
        Returns:
            Dictionary with client configuration parameters
        """
        return {
            "aws_region": self._region
        }
    
    def get_boto3_client_config(self) -> Dict[str, str]:
        """
        Get configuration dictionary for boto3 bedrock-runtime client.
        
        Returns:
            Dictionary with boto3 client configuration parameters
        """
        return {
            "region_name": self._region
        }


# Global default instance for easy access
default_config = ConfigManager()