"""
Standalone test script that doesn't require pipenv.
Run with: python test_render_standalone.py
Make sure you're in the 3-python-package-brio directory.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from minecraft_textcraft import (
    render,
    renderTextOnly,
    renderCommandOnly,
    renderTextAndCommands,
)


def print_test_header(test_num, description):
    """Print a formatted test header"""
    print("=" * 70)
    print(f"TEST {test_num}: {description}")
    print("=" * 70)
    print()


def print_input_output(input_text, output_text, input_type="Text"):
    """Print what we're testing and the result"""
    print(f"📥 {input_type}: {repr(input_text)}")
    print()
    print("📤 Output:")
    print("-" * 70)
    print(output_text)
    print("-" * 70)
    print()


def test_render_text_only():
    """Test rendering text only"""
    print_test_header(1, "Render Text Only")
    input_text = "HELLO"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Text")
    print()


def test_render_numbers():
    """Test rendering numbers"""
    print_test_header(2, "Render Numbers")
    input_text = "12345"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Text")
    print()


def test_render_command_only_sword():
    """Test rendering sword command"""
    print_test_header(3, "Render Command Only - Sword")
    command_name = "sword"
    result = renderCommandOnly(command_name)
    print_input_output(command_name, result, "Command")
    print()


def test_render_command_only_earth():
    """Test rendering earth command"""
    print_test_header(4, "Render Command Only - Earth")
    command_name = "earth"
    result = renderCommandOnly(command_name)
    print_input_output(command_name, result, "Command")
    print()


def test_render_mixed_text_and_sword():
    """Test rendering text with sword command"""
    print_test_header(5, "Render Mixed Text and Commands - Sword")
    input_text = "GET \\\\sword NOW"
    result = renderTextAndCommands(input_text)
    print_input_output(input_text, result, "Mixed Text")
    print()


def test_render_mixed_text_and_earth():
    """Test rendering text with earth command"""
    print_test_header(6, "Render Mixed Text and Commands - Earth")
    input_text = "HELLO \\\\earth WORLD"
    result = renderTextAndCommands(input_text)
    print_input_output(input_text, result, "Mixed Text")
    print()


def test_render_main_text_only():
    """Test the main render function with text only"""
    print_test_header(7, "Main Render Function - Text Only")
    input_text = "MINECRAFT"
    result = render(input_text)
    print_input_output(input_text, result, "Text")
    print()


def test_render_main_command_only():
    """Test the main render function with command only"""
    print_test_header(8, "Main Render Function - Command Only (Sword)")
    input_text = "\\\\sword"
    result = render(input_text)
    print_input_output(input_text, result, "Command")
    print()


def test_render_main_mixed():
    """Test the main render function with mixed input"""
    print_test_header(9, "Main Render Function - Mixed (Text + Sword)")
    input_text = "GET \\\\sword NOW"
    result = render(input_text)
    print_input_output(input_text, result, "Mixed")
    print()


def test_render_main_multiple_commands():
    """Test the main render function with multiple commands"""
    print_test_header(10, "Main Render Function - Multiple Commands")
    input_text = "\\\\sword \\\\earth \\\\sword"
    result = render(input_text)
    print_input_output(input_text, result, "Multiple Commands")
    print()


def test_edge_case_empty_string():
    """Test edge case: empty string"""
    print_test_header(11, "Edge Case - Empty String")
    input_text = ""
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Empty String")
    print()


def test_edge_case_whitespace_only():
    """Test edge case: whitespace only"""
    print_test_header(12, "Edge Case - Whitespace Only")
    input_text = "   "
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Whitespace Only")
    print()


def test_edge_case_invalid_characters():
    """Test edge case: invalid characters (should raise error)"""
    print_test_header(13, "Edge Case - Invalid Characters")
    input_text = "HELLO!"
    try:
        result = renderTextOnly(input_text)
        print_input_output(input_text, result, "Invalid Characters")
        print("⚠️  WARNING: Should have raised ValueError!")
    except ValueError as e:
        print(f"📥 Input: {repr(input_text)}")
        print(f"✅ Correctly raised ValueError: {e}")
    print()


def test_edge_case_invalid_command():
    """Test edge case: invalid command (should raise error)"""
    print_test_header(14, "Edge Case - Invalid Command")
    command_name = "invalid_command"
    try:
        result = renderCommandOnly(command_name)
        print_input_output(command_name, result, "Invalid Command")
        print("⚠️  WARNING: Should have raised ValueError!")
    except ValueError as e:
        print(f"📥 Command: {repr(command_name)}")
        print(f"✅ Correctly raised ValueError: {e}")
    print()


def test_edge_case_malformed_command():
    """Test edge case: malformed command (should raise error)"""
    print_test_header(15, "Edge Case - Malformed Command")
    input_text = "HELLO \\\\ WORLD"
    try:
        result = renderTextAndCommands(input_text)
        print_input_output(input_text, result, "Malformed Command")
        print("⚠️  WARNING: Should have raised ValueError!")
    except ValueError as e:
        print(f"📥 Input: {repr(input_text)}")
        print(f"✅ Correctly raised ValueError: {e}")
    print()


def test_text_with_spaces():
    """Test text with spaces"""
    print_test_header(16, "Text with Spaces")
    input_text = "HELLO WORLD"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Text with Spaces")
    print()


def test_mixed_uppercase_lowercase():
    """Test mixed case (should be converted to uppercase)"""
    print_test_header(17, "Mixed Case Text (Auto-uppercase)")
    input_text = "Hello World 123"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Mixed Case")
    print()


def test_multiple_commands_only():
    """Test multiple commands without text"""
    print_test_header(18, "Multiple Commands Only")
    input_text = "\\\\sword \\\\earth"
    result = render(input_text)
    print_input_output(input_text, result, "Multiple Commands")
    print()


def test_commands_at_start():
    """Test command at the start of text"""
    print_test_header(19, "Command at Start")
    input_text = "\\\\sword HELLO"
    result = render(input_text)
    print_input_output(input_text, result, "Command at Start")
    print()


def test_commands_at_end():
    """Test command at the end of text"""
    print_test_header(20, "Command at End")
    input_text = "HELLO \\\\sword"
    result = render(input_text)
    print_input_output(input_text, result, "Command at End")
    print()


def test_multiple_commands_with_text():
    """Test multiple commands interspersed with text"""
    print_test_header(21, "Multiple Commands with Text")
    input_text = "GET \\\\sword AND \\\\earth NOW"
    result = render(input_text)
    print_input_output(input_text, result, "Multiple Commands with Text")
    print()


def test_consecutive_commands():
    """Test consecutive commands"""
    print_test_header(22, "Consecutive Commands")
    input_text = "\\\\sword\\\\earth\\\\sword"
    result = render(input_text)
    print_input_output(input_text, result, "Consecutive Commands")
    print()


def test_single_character():
    """Test single character rendering"""
    print_test_header(23, "Single Character")
    input_text = "A"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Single Character")
    print()


def test_single_digit():
    """Test single digit rendering"""
    print_test_header(24, "Single Digit")
    input_text = "5"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Single Digit")
    print()


def test_long_text():
    """Test long text string"""
    print_test_header(25, "Long Text String")
    input_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Long Text")
    print()


def test_text_with_only_spaces():
    """Test text with only spaces between characters"""
    print_test_header(26, "Text with Only Spaces")
    input_text = "A B C D"
    result = renderTextOnly(input_text)
    print_input_output(input_text, result, "Text with Spaces")
    print()


if __name__ == "__main__":
    try:
        test_render_text_only()
        test_render_numbers()
        test_render_command_only_sword()
        test_render_command_only_earth()
        test_render_mixed_text_and_sword()
        test_render_mixed_text_and_earth()
        test_render_main_text_only()
        test_render_main_command_only()
        test_render_main_mixed()
        test_render_main_multiple_commands()
        test_edge_case_empty_string()
        test_edge_case_whitespace_only()
        test_edge_case_invalid_characters()
        test_edge_case_invalid_command()
        test_edge_case_malformed_command()
        test_text_with_spaces()
        test_mixed_uppercase_lowercase()
        test_multiple_commands_only()
        test_commands_at_start()
        test_commands_at_end()
        test_multiple_commands_with_text()
        test_consecutive_commands()
        test_single_character()
        test_single_digit()
        test_long_text()
        test_text_with_only_spaces()

        print("=" * 70)
        print("✅ All tests completed successfully!")
        print("=" * 70)
    except Exception as e:
        print("=" * 70)
        print(f"❌ ERROR: {e}")
        print("=" * 70)
        import traceback

        traceback.print_exc()
