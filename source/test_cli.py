"""
Test script for CLI tools.
Tests basic functionality without making actual API calls.
"""
import sys
from io import StringIO
from unittest.mock import patch, MagicMock
import tempfile
import os


def test_module_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")
    try:
        import base_cli
        import importlib
        
        # Import modules with hyphens in their names
        modules = [
            'ask-me-anything',
            'formal-text-with-bedrock',
            'translate-article-to-english',
            'translate-article-to-taiwannese',
            'summarize-taiwanese-text-with-bedrock',
            'summarize-text-with-bedrock',
            'generate-taiwan-meeting-summarize',
            'AnthropicBedrock'
        ]
        
        for module_name in modules:
            importlib.import_module(module_name)
        
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_load_input():
    """Test input loading functionality."""
    print("\nTesting input loading...")
    from base_cli import load_input
    
    # Test direct text input
    result = load_input("test text", None)
    assert result == "test text", "Direct text input failed"
    print("✓ Direct text input works")
    
    # Test file input
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        f.write("file content")
        temp_path = f.name
    
    try:
        result = load_input(None, temp_path)
        assert result == "file content", "File input failed"
        print("✓ File input works")
    finally:
        os.unlink(temp_path)
    
    return True


def test_save_output():
    """Test output saving functionality."""
    print("\nTesting output saving...")
    from base_cli import save_output
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
        temp_path = f.name
    
    try:
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        save_output("test content", temp_path, "Success!")
        
        # Restore stdout
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        # Verify file content
        with open(temp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        assert content == "test content", "File content mismatch"
        assert "Success!" in output, "Success message not printed"
        print("✓ Output saving works")
    finally:
        os.unlink(temp_path)
    
    return True


def test_stream_response_mock():
    """Test stream_response with mocked API."""
    print("\nTesting stream response (mocked)...")
    from base_cli import stream_response
    
    # Mock the AnthropicBedrock client
    with patch('base_cli.AnthropicBedrock') as mock_client:
        # Create mock stream
        mock_chunk = MagicMock()
        mock_chunk.type = "content_block_delta"
        mock_chunk.delta.text = "test response"
        
        mock_stream = MagicMock()
        mock_stream.__enter__ = MagicMock(return_value=[mock_chunk])
        mock_stream.__exit__ = MagicMock(return_value=False)
        
        mock_instance = MagicMock()
        mock_instance.messages.create.return_value = mock_stream
        mock_client.return_value = mock_instance
        
        # Test the function
        result = list(stream_response("test input"))
        assert result == ["test response"], "Stream response failed"
        print("✓ Stream response works (mocked)")
    
    return True


def test_prompt_builders():
    """Test prompt builder functions."""
    print("\nTesting prompt builders...")
    import importlib
    
    modules_to_test = {
        'formal-text-with-bedrock': 'Formal text',
        'translate-article-to-english': 'Translation to English',
        'translate-article-to-taiwannese': 'Translation to Chinese',
        'summarize-taiwanese-text-with-bedrock': 'Taiwanese summarization',
        'summarize-text-with-bedrock': 'Text summarization',
        'generate-taiwan-meeting-summarize': 'Meeting summary',
        'ask-me-anything': 'Ask me anything',
        'AnthropicBedrock': 'Generic summarization'
    }
    
    for module_name, description in modules_to_test.items():
        module = importlib.import_module(module_name)
        assert callable(module.main), f"{description} main not callable"
        print(f"✓ {description} module has main function")
    
    return True


def test_config_manager():
    """Test configuration manager."""
    print("\nTesting configuration manager...")
    from config_manager import ConfigManager, default_config
    
    # Test default config
    assert default_config is not None, "Default config not initialized"
    print("✓ Default config exists")
    
    # Test model ID validation
    assert default_config.validate_model_id("global.anthropic.claude-sonnet-4-5-20250929-v1:0"), "Valid model ID rejected"
    print("✓ Model ID validation works")
    
    # Test region validation
    assert default_config.validate_region("ap-northeast-1"), "Valid region rejected"
    print("✓ Region validation works")
    
    return True


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("Running CLI Tests")
    print("=" * 60)
    
    tests = [
        test_module_imports,
        test_config_manager,
        test_load_input,
        test_save_output,
        test_stream_response_mock,
        test_prompt_builders,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
