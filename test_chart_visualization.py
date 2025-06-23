#!/usr/bin/env python3
"""
Test script for chart visualization functionality
Demonstrates PNG and HTML output generation
"""
import json
import os
import subprocess
import sys

def test_chart_visualization():
    """Test the chart visualization with sample data"""
    
    # Sample data for testing
    test_data = [
        {"Product": "Product A", "Sales": 1200, "Region": "North"},
        {"Product": "Product B", "Sales": 1800, "Region": "North"},
        {"Product": "Product C", "Sales": 900, "Region": "North"},
        {"Product": "Product A", "Sales": 1500, "Region": "South"},
        {"Product": "Product B", "Sales": 2100, "Region": "South"},
        {"Product": "Product C", "Sales": 1100, "Region": "South"}
    ]
    
    # Test configuration
    test_config = {
        "llm_config": {
            "base_url": "http://localhost",
            "model": "test-model",
            "api_key": "test-key"
        },
        "dataset": test_data,
        "user_prompt": "Sales comparison by product and region",
        "file_name": "sales_comparison",
        "task_type": "visualization",
        "directory": "/home/user/workspace/workspace",
        "language": "en"
    }
    
    # Test HTML output
    print("Testing HTML output...")
    html_config = test_config.copy()
    html_config["output_type"] = "html"
    html_config["file_name"] = "sales_comparison_html"
    
    result = run_chart_visualization(html_config)
    if result:
        print(f"✅ HTML chart generated successfully: {result}")
    else:
        print("❌ HTML chart generation failed")
    
    # Test PNG output
    print("\nTesting PNG output...")
    png_config = test_config.copy()
    png_config["output_type"] = "png"
    png_config["file_name"] = "sales_comparison_png"
    
    result = run_chart_visualization(png_config)
    if result:
        print(f"✅ PNG chart generated successfully: {result}")
    else:
        print("❌ PNG chart generation failed")

def run_chart_visualization(config):
    """Run the chart visualization with given config"""
    try:
        # Convert config to JSON
        config_json = json.dumps(config)
        
        # Run the TypeScript chart visualization
        process = subprocess.run(
            ["npx", "ts-node", "src/chartVisualize.ts"],
            input=config_json,
            text=True,
            capture_output=True,
            cwd="/home/user/workspace/app/tool/chart_visualization"
        )
        
        if process.returncode == 0:
            result = json.loads(process.stdout.strip())
            return result.get("chart_path")
        else:
            print(f"Error: {process.stderr}")
            return None
            
    except Exception as e:
        print(f"Exception: {e}")
        return None

def list_generated_files():
    """List all generated files in the workspace"""
    viz_dir = "/home/user/workspace/workspace/visualization"
    if os.path.exists(viz_dir):
        print(f"\nGenerated files in {viz_dir}:")
        for file in os.listdir(viz_dir):
            file_path = os.path.join(viz_dir, file)
            size = os.path.getsize(file_path)
            print(f"  📄 {file} ({size} bytes)")
    else:
        print(f"\nVisualization directory {viz_dir} does not exist")

if __name__ == "__main__":
    print("🚀 Testing Chart Visualization Functionality")
    print("=" * 50)
    
    test_chart_visualization()
    list_generated_files()
    
    print("\n✨ Chart visualization test completed!")
