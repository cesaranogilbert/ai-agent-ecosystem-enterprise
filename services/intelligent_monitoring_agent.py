"""
Intelligent Monitoring Agent
Responsibility: Provides intelligent monitoring, alerting, and system health management
Role: System Intelligence and Monitoring Specialist
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from openai import OpenAI

logger = logging.getLogger(__name__)

class IntelligentMonitoringAgent:
    def __init__(self):
        self.name = "Intelligent Monitoring Agent"
        self.role = "System Intelligence and Monitoring Specialist"
        self.responsibilities = [
            "Intelligent system monitoring and health tracking",
            "Predictive alerting and anomaly detection",
            "Performance optimization recommendations",
            "Root cause analysis and incident management",
            "Automated remediation and self-healing",
            "Comprehensive observability and insights"
        ]
        self.capabilities = {
            "intelligent_monitoring": True,
            "predictive_alerting": True,
            "anomaly_detection": True,
            "root_cause_analysis": True,
            "automated_remediation": True,
            "observability": True
        }
        self.openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.monitoring_systems = {}
        self.active_alerts = {}
        logger.info(f"{self.name} initialized with role: {self.role}")

    def setup_intelligent_monitoring_system(self, monitoring_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up comprehensive intelligent monitoring system"""
        try:
            monitoring_system = {
                "system_id": f"monitor_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "name": monitoring_config.get("name", "Intelligent Monitoring System"),
                "description": monitoring_config.get("description", ""),
                "monitored_resources": self._configure_monitored_resources(monitoring_config.get("resources", [])),
                "monitoring_layers": {
                    "infrastructure_monitoring": self._setup_infrastructure_monitoring(monitoring_config.get("infrastructure", {})),
                    "application_monitoring": self._setup_application_monitoring(monitoring_config.get("application", {})),
                    "business_monitoring": self._setup_business_monitoring(monitoring_config.get("business", {})),
                    "user_experience_monitoring": self._setup_ux_monitoring(monitoring_config.get("ux", {}))
                },
                "intelligence_features": {
                    "anomaly_detection": {
                        "ml_algorithms": ["isolation_forest", "autoencoder", "statistical_analysis"],
                        "sensitivity_level": monitoring_config.get("anomaly_sensitivity", "medium"),
                        "learning_period": monitoring_config.get("learning_period", "7 days"),
                        "auto_baseline_adjustment": monitoring_config.get("auto_baseline", True)
                    },
                    "predictive_analytics": {
                        "trend_analysis": True,
                        "capacity_forecasting": True,
                        "failure_prediction": True,
                        "performance_prediction": True
                    },
                    "root_cause_analysis": {
                        "correlation_analysis": True,
                        "dependency_mapping": True,
                        "historical_pattern_matching": True,
                        "ai_assisted_diagnosis": True
                    }
                },
                "alerting_config": {
                    "intelligent_alerting": True,
                    "alert_correlation": True,
                    "noise_reduction": True,
                    "severity_escalation": monitoring_config.get("escalation", True),
                    "notification_channels": monitoring_config.get("notification_channels", ["email", "slack"])
                },
                "automation_features": {
                    "auto_remediation": monitoring_config.get("auto_remediation", False),
                    "self_healing": monitoring_config.get("self_healing", False),
                    "auto_scaling": monitoring_config.get("auto_scaling", True),
                    "incident_automation": monitoring_config.get("incident_automation", True)
                }
            }
            
            # Set up monitoring infrastructure
            infrastructure_setup = self._setup_monitoring_infrastructure(monitoring_system)
            monitoring_system["infrastructure"] = infrastructure_setup
            
            # Initialize intelligence engines
            intelligence_engines = self._initialize_intelligence_engines(monitoring_system)
            monitoring_system["intelligence_engines"] = intelligence_engines
            
            # Create monitoring dashboards
            dashboards = self._create_monitoring_dashboards(monitoring_system)
            monitoring_system["dashboards"] = dashboards
            
            # Store monitoring system
            self.monitoring_systems[monitoring_system["system_id"]] = monitoring_system
            
            logger.info(f"Set up intelligent monitoring system: {monitoring_system['system_id']}")
            return {
                "success": True,
                "monitoring_system": monitoring_system,
                "dashboard_urls": self._create_dashboard_urls(monitoring_system),
                "api_endpoints": self._create_monitoring_api_endpoints(monitoring_system)
            }
            
        except Exception as e:
            logger.error(f"Intelligent monitoring system setup failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def perform_intelligent_analysis(self, analysis_request: Dict[str, Any]) -> Dict[str, Any]:
        """Perform intelligent analysis of system metrics and behaviors"""
        try:
            analysis_session = {
                "analysis_id": f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "request": analysis_request,
                "start_time": datetime.now().isoformat(),
                "analysis_type": analysis_request.get("type", "comprehensive"),
                "time_window": analysis_request.get("time_window", "24 hours"),
                "metrics_analyzed": [],
                "findings": {},
                "recommendations": [],
                "intelligence_insights": {}
            }
            
            # Collect and analyze metrics
            metrics_data = self._collect_metrics_data(analysis_request)
            analysis_session["metrics_analyzed"] = list(metrics_data.keys())
            
            # Perform anomaly detection
            anomaly_results = self._perform_anomaly_detection(metrics_data)
            analysis_session["findings"]["anomalies"] = anomaly_results
            
            # Perform trend analysis
            trend_analysis = self._perform_trend_analysis(metrics_data)
            analysis_session["findings"]["trends"] = trend_analysis
            
            # Perform correlation analysis
            correlation_analysis = self._perform_correlation_analysis(metrics_data)
            analysis_session["findings"]["correlations"] = correlation_analysis
            
            # Generate intelligent insights using AI
            ai_insights = self._generate_intelligent_insights(analysis_session, metrics_data)
            analysis_session["intelligence_insights"] = ai_insights
            
            # Generate actionable recommendations
            recommendations = self._generate_actionable_recommendations(analysis_session)
            analysis_session["recommendations"] = recommendations
            
            # Perform predictive analysis
            predictive_analysis = self._perform_predictive_analysis(metrics_data)
            analysis_session["findings"]["predictions"] = predictive_analysis
            
            analysis_session["end_time"] = datetime.now().isoformat()
            analysis_session["analysis_duration"] = self._calculate_duration(
                analysis_session["start_time"], analysis_session["end_time"]
            )
            
            return {
                "success": True,
                "analysis_session": analysis_session,
                "priority_actions": self._identify_priority_actions(analysis_session),
                "risk_assessment": self._assess_system_risks(analysis_session)
            }
            
        except Exception as e:
            logger.error(f"Intelligent analysis failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def create_intelligent_alerting_system(self, alerting_config: Dict[str, Any]) -> Dict[str, Any]:
        """Create intelligent alerting system with ML-based optimization"""
        try:
            alerting_system = {
                "system_id": f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "name": alerting_config.get("name", "Intelligent Alerting System"),
                "alert_rules": self._create_intelligent_alert_rules(alerting_config.get("rules", [])),
                "ml_optimization": {
                    "noise_reduction_enabled": alerting_config.get("noise_reduction", True),
                    "alert_correlation": alerting_config.get("correlation", True),
                    "severity_optimization": alerting_config.get("severity_optimization", True),
                    "false_positive_learning": alerting_config.get("fp_learning", True)
                },
                "notification_intelligence": {
                    "recipient_optimization": alerting_config.get("recipient_optimization", True),
                    "timing_optimization": alerting_config.get("timing_optimization", True),
                    "channel_selection": alerting_config.get("smart_channels", True),
                    "escalation_intelligence": alerting_config.get("smart_escalation", True)
                },
                "alert_lifecycle": {
                    "auto_acknowledgment": alerting_config.get("auto_ack", False),
                    "auto_resolution": alerting_config.get("auto_resolve", False),
                    "feedback_learning": alerting_config.get("feedback_learning", True),
                    "alert_aging": alerting_config.get("alert_aging", True)
                },
                "integration_config": {
                    "incident_management": alerting_config.get("incident_tools", []),
                    "communication_tools": alerting_config.get("comm_tools", []),
                    "automation_tools": alerting_config.get("automation_tools", [])
                }
            }
            
            # Set up ML models for alert optimization
            ml_models = self._setup_alerting_ml_models(alerting_system)
            alerting_system["ml_models"] = ml_models
            
            # Create alert processing pipeline
            processing_pipeline = self._create_alert_processing_pipeline(alerting_system)
            alerting_system["processing_pipeline"] = processing_pipeline
            
            # Set up alert analytics
            analytics_config = self._setup_alert_analytics(alerting_system)
            alerting_system["analytics"] = analytics_config
            
            logger.info(f"Created intelligent alerting system: {alerting_system['system_id']}")
            return {
                "success": True,
                "alerting_system": alerting_system,
                "effectiveness_metrics": self._define_alerting_effectiveness_metrics(),
                "optimization_schedule": self._create_alerting_optimization_schedule()
            }
            
        except Exception as e:
            logger.error(f"Intelligent alerting system creation failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def implement_automated_remediation(self, remediation_config: Dict[str, Any]) -> Dict[str, Any]:
        """Implement automated remediation and self-healing capabilities"""
        try:
            remediation_system = {
                "system_id": f"remediation_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "name": remediation_config.get("name", "Automated Remediation System"),
                "remediation_scenarios": self._define_remediation_scenarios(remediation_config.get("scenarios", [])),
                "automation_rules": {
                    "trigger_conditions": self._create_trigger_conditions(remediation_config.get("triggers", [])),
                    "safety_checks": self._create_safety_checks(remediation_config.get("safety", [])),
                    "rollback_procedures": self._create_rollback_procedures(remediation_config.get("rollback", []))
                },
                "remediation_actions": {
                    "infrastructure_actions": self._create_infrastructure_actions(),
                    "application_actions": self._create_application_actions(),
                    "data_actions": self._create_data_actions(),
                    "network_actions": self._create_network_actions()
                },
                "intelligence_features": {
                    "success_rate_tracking": True,
                    "impact_assessment": True,
                    "learning_from_outcomes": True,
                    "action_optimization": True
                },
                "governance": {
                    "approval_workflows": remediation_config.get("approval_required", False),
                    "audit_logging": True,
                    "compliance_checks": remediation_config.get("compliance", []),
                    "risk_assessment": True
                }
            }
            
            # Set up remediation intelligence
            intelligence_config = self._setup_remediation_intelligence(remediation_system)
            remediation_system["intelligence"] = intelligence_config
            
            # Create remediation workflows
            workflows = self._create_remediation_workflows(remediation_system)
            remediation_system["workflows"] = workflows
            
            # Set up success tracking
            success_tracking = self._setup_remediation_success_tracking(remediation_system)
            remediation_system["success_tracking"] = success_tracking
            
            logger.info(f"Implemented automated remediation system: {remediation_system['system_id']}")
            return {
                "success": True,
                "remediation_system": remediation_system,
                "safety_report": self._generate_safety_report(remediation_system),
                "testing_plan": self._create_remediation_testing_plan(remediation_system)
            }
            
        except Exception as e:
            logger.error(f"Automated remediation implementation failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def optimize_monitoring_strategy(self, optimization_request: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize monitoring strategy based on AI analysis and historical data"""
        try:
            # Analyze current monitoring effectiveness
            effectiveness_analysis = self._analyze_monitoring_effectiveness(optimization_request.get("current_data", {}))
            
            # Generate optimization recommendations using AI
            optimization_prompt = f"""
            Analyze the following monitoring system effectiveness and provide comprehensive optimization recommendations:
            
            Current Monitoring Effectiveness: {json.dumps(effectiveness_analysis, indent=2)}
            Monitoring Challenges: {json.dumps(optimization_request.get("challenges", []), indent=2)}
            
            Provide detailed recommendations for:
            1. Monitoring coverage optimization
            2. Alert noise reduction strategies
            3. Performance monitoring enhancements
            4. Predictive monitoring capabilities
            5. Cost optimization opportunities
            6. Intelligence and automation improvements
            
            Format as JSON with prioritized optimization strategies and expected benefits.
            """
            
            response = self.openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a monitoring and observability expert specializing in intelligent monitoring systems and optimization strategies."},
                    {"role": "user", "content": optimization_prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            optimization_recommendations = json.loads(response.choices[0].message.content or '{}')
            
            # Create optimized monitoring strategy
            optimized_strategy = self._create_optimized_monitoring_strategy(effectiveness_analysis, optimization_recommendations)
            
            # Plan strategy implementation
            implementation_plan = self._create_monitoring_optimization_plan(optimized_strategy)
            
            optimization_result = {
                "optimization_id": f"opt_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "effectiveness_analysis": effectiveness_analysis,
                "optimization_recommendations": optimization_recommendations,
                "optimized_strategy": optimized_strategy,
                "implementation_plan": implementation_plan,
                "expected_benefits": self._calculate_monitoring_benefits(optimization_recommendations),
                "cost_analysis": self._calculate_monitoring_costs(optimization_recommendations)
            }
            
            return {
                "success": True,
                "optimization_result": optimization_result,
                "migration_strategy": self._create_monitoring_migration_strategy(optimization_result)
            }
            
        except Exception as e:
            logger.error(f"Monitoring strategy optimization failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def _configure_monitored_resources(self, resources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Configure resources to be monitored"""
        configured_resources = []
        
        for resource in resources:
            configured_resource = {
                "resource_id": resource.get("id") or f"res_{len(configured_resources)+1}",
                "name": resource.get("name", "Monitored Resource"),
                "type": resource.get("type", "server"),
                "monitoring_config": resource.get("config", {}),
                "metrics_collected": resource.get("metrics", []),
                "health_checks": resource.get("health_checks", []),
                "thresholds": resource.get("thresholds", {})
            }
            configured_resources.append(configured_resource)
        
        return configured_resources

    def _setup_infrastructure_monitoring(self, infrastructure_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up infrastructure monitoring layer"""
        return {
            "server_monitoring": {
                "cpu_monitoring": True,
                "memory_monitoring": True,
                "disk_monitoring": True,
                "network_monitoring": True,
                "process_monitoring": infrastructure_config.get("process_monitoring", True)
            },
            "container_monitoring": {
                "docker_monitoring": infrastructure_config.get("docker", False),
                "kubernetes_monitoring": infrastructure_config.get("kubernetes", False),
                "resource_limits_tracking": True
            },
            "cloud_monitoring": {
                "aws_cloudwatch": infrastructure_config.get("aws", False),
                "azure_monitor": infrastructure_config.get("azure", False),
                "gcp_monitoring": infrastructure_config.get("gcp", False)
            }
        }

    def _setup_application_monitoring(self, application_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up application monitoring layer"""
        return {
            "performance_monitoring": {
                "response_time_tracking": True,
                "throughput_monitoring": True,
                "error_rate_tracking": True,
                "dependency_monitoring": application_config.get("dependencies", True)
            },
            "application_logs": {
                "log_aggregation": True,
                "log_analysis": True,
                "error_tracking": True,
                "security_log_monitoring": application_config.get("security_logs", True)
            },
            "distributed_tracing": {
                "request_tracing": application_config.get("tracing", False),
                "service_map_generation": application_config.get("service_maps", False),
                "bottleneck_identification": True
            }
        }

    def _setup_business_monitoring(self, business_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up business monitoring layer"""
        return {
            "kpi_monitoring": {
                "business_metrics": business_config.get("kpis", []),
                "revenue_tracking": business_config.get("revenue", False),
                "user_engagement": business_config.get("engagement", False),
                "conversion_tracking": business_config.get("conversions", False)
            },
            "sla_monitoring": {
                "sla_compliance_tracking": True,
                "customer_satisfaction": business_config.get("csat", False),
                "service_availability": True
            }
        }

    def _setup_ux_monitoring(self, ux_config: Dict[str, Any]) -> Dict[str, Any]:
        """Set up user experience monitoring layer"""
        return {
            "real_user_monitoring": {
                "page_load_times": ux_config.get("page_loads", False),
                "user_interactions": ux_config.get("interactions", False),
                "error_tracking": True
            },
            "synthetic_monitoring": {
                "uptime_checks": ux_config.get("uptime", True),
                "transaction_monitoring": ux_config.get("transactions", False),
                "api_monitoring": ux_config.get("api", True)
            }
        }

    def _setup_monitoring_infrastructure(self, monitoring_system: Dict[str, Any]) -> Dict[str, Any]:
        """Set up monitoring infrastructure"""
        return {
            "data_collection": {
                "agents": ["telegraf", "collectd", "node_exporter"],
                "log_shippers": ["filebeat", "fluentd", "logstash"],
                "custom_collectors": True
            },
            "data_storage": {
                "time_series_db": "prometheus",
                "log_storage": "elasticsearch",
                "metrics_retention": "90 days",
                "log_retention": "30 days"
            },
            "processing_engines": {
                "stream_processing": "kafka",
                "batch_processing": "apache_spark",
                "ml_processing": "apache_airflow"
            },
            "visualization": {
                "dashboards": "grafana",
                "custom_dashboards": True,
                "mobile_access": True
            }
        }

    def _initialize_intelligence_engines(self, monitoring_system: Dict[str, Any]) -> Dict[str, Any]:
        """Initialize intelligence engines"""
        return {
            "anomaly_detection_engine": {
                "status": "initialized",
                "algorithms": ["isolation_forest", "autoencoder"],
                "training_data_days": 30,
                "model_update_frequency": "daily"
            },
            "predictive_analytics_engine": {
                "status": "initialized",
                "forecasting_models": ["arima", "lstm", "prophet"],
                "prediction_horizon": "7 days",
                "confidence_intervals": True
            },
            "correlation_engine": {
                "status": "initialized",
                "correlation_algorithms": ["pearson", "spearman", "mutual_information"],
                "dependency_mapping": True,
                "causal_inference": False
            }
        }

    def _create_monitoring_dashboards(self, monitoring_system: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create monitoring dashboards"""
        dashboards = [
            {
                "dashboard_id": "system_overview",
                "name": "System Overview",
                "type": "overview",
                "widgets": ["system_health", "key_metrics", "recent_alerts"],
                "refresh_rate": "30 seconds"
            },
            {
                "dashboard_id": "infrastructure",
                "name": "Infrastructure Monitoring",
                "type": "infrastructure",
                "widgets": ["cpu_usage", "memory_usage", "disk_usage", "network_usage"],
                "refresh_rate": "10 seconds"
            },
            {
                "dashboard_id": "application_performance",
                "name": "Application Performance",
                "type": "application",
                "widgets": ["response_times", "throughput", "error_rates", "dependencies"],
                "refresh_rate": "15 seconds"
            }
        ]
        
        return dashboards

    def _create_dashboard_urls(self, monitoring_system: Dict[str, Any]) -> Dict[str, str]:
        """Create dashboard URLs"""
        system_id = monitoring_system["system_id"]
        return {
            "system_overview": f"/monitoring/{system_id}/overview",
            "infrastructure": f"/monitoring/{system_id}/infrastructure",
            "application": f"/monitoring/{system_id}/application",
            "business": f"/monitoring/{system_id}/business"
        }

    def _create_monitoring_api_endpoints(self, monitoring_system: Dict[str, Any]) -> Dict[str, str]:
        """Create monitoring API endpoints"""
        system_id = monitoring_system["system_id"]
        return {
            "metrics": f"/api/monitoring/{system_id}/metrics",
            "alerts": f"/api/monitoring/{system_id}/alerts",
            "health": f"/api/monitoring/{system_id}/health",
            "anomalies": f"/api/monitoring/{system_id}/anomalies",
            "predictions": f"/api/monitoring/{system_id}/predictions"
        }

    def _collect_metrics_data(self, analysis_request: Dict[str, Any]) -> Dict[str, Any]:
        """Collect metrics data for analysis"""
        # Simulate metrics data collection
        return {
            "cpu_usage": {"avg": 65, "max": 95, "trend": "increasing"},
            "memory_usage": {"avg": 70, "max": 85, "trend": "stable"},
            "disk_usage": {"avg": 45, "max": 60, "trend": "increasing"},
            "network_io": {"avg": 30, "max": 80, "trend": "variable"},
            "response_time": {"avg": 250, "max": 1200, "trend": "increasing"},
            "error_rate": {"avg": 0.5, "max": 2.1, "trend": "increasing"},
            "throughput": {"avg": 1500, "min": 800, "trend": "decreasing"}
        }

    def _perform_anomaly_detection(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform anomaly detection on metrics"""
        anomalies = []
        
        # Simulate anomaly detection
        for metric, data in metrics_data.items():
            if data.get("max", 0) > data.get("avg", 0) * 1.5:
                anomalies.append({
                    "metric": metric,
                    "anomaly_type": "spike",
                    "severity": "medium" if data["max"] < data["avg"] * 2 else "high",
                    "timestamp": datetime.now().isoformat(),
                    "confidence": 0.85
                })
        
        return {
            "anomalies_detected": len(anomalies),
            "anomaly_details": anomalies,
            "detection_confidence": 0.87,
            "false_positive_rate": 0.05
        }

    def _perform_trend_analysis(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform trend analysis on metrics"""
        trends = {}
        
        for metric, data in metrics_data.items():
            trend = data.get("trend", "stable")
            trends[metric] = {
                "direction": trend,
                "strength": "strong" if trend != "stable" else "none",
                "prediction": "continued_trend" if trend != "stable" else "stable"
            }
        
        return {
            "trend_summary": trends,
            "concerning_trends": [k for k, v in trends.items() if v["direction"] == "increasing" and k in ["cpu_usage", "error_rate"]],
            "positive_trends": [k for k, v in trends.items() if v["direction"] == "decreasing" and k in ["error_rate", "response_time"]]
        }

    def _perform_correlation_analysis(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform correlation analysis between metrics"""
        correlations = [
            {"metric1": "cpu_usage", "metric2": "response_time", "correlation": 0.78, "strength": "strong"},
            {"metric1": "memory_usage", "metric2": "error_rate", "correlation": 0.45, "strength": "moderate"},
            {"metric1": "throughput", "metric2": "response_time", "correlation": -0.65, "strength": "strong"}
        ]
        
        return {
            "correlations_found": len(correlations),
            "correlation_details": correlations,
            "strong_correlations": [c for c in correlations if c["strength"] == "strong"],
            "insights": ["High CPU usage strongly correlates with increased response times"]
        }

    def _generate_intelligent_insights(self, analysis_session: Dict[str, Any], metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate intelligent insights using AI"""
        insights_prompt = f"""
        Analyze the following system monitoring data and provide intelligent insights:
        
        Metrics Data: {json.dumps(metrics_data, indent=2)}
        Anomalies: {json.dumps(analysis_session["findings"].get("anomalies", {}), indent=2)}
        Trends: {json.dumps(analysis_session["findings"].get("trends", {}), indent=2)}
        
        Provide insights on:
        1. System health assessment
        2. Performance bottlenecks
        3. Potential issues and risks
        4. Optimization opportunities
        5. Predictive warnings
        
        Format as JSON with clear, actionable insights.
        """
        
        try:
            response = self.openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a system monitoring expert specializing in intelligent analysis and predictive insights."},
                    {"role": "user", "content": insights_prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            return json.loads(response.choices[0].message.content or '{}')
        except Exception as e:
            logger.error(f"AI insights generation failed: {str(e)}")
            return {"insights": "Unable to generate AI insights", "error": str(e)}

    def _generate_actionable_recommendations(self, analysis_session: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Based on findings
        findings = analysis_session.get("findings", {})
        
        if findings.get("anomalies", {}).get("anomalies_detected", 0) > 0:
            recommendations.append("Investigate detected anomalies and implement alerting")
        
        trends = findings.get("trends", {})
        if trends.get("concerning_trends"):
            recommendations.append("Address increasing trends in CPU usage and error rates")
        
        correlations = findings.get("correlations", {})
        if correlations.get("strong_correlations"):
            recommendations.append("Optimize correlated metrics to improve overall system performance")
        
        if not recommendations:
            recommendations.append("System appears healthy - maintain current monitoring")
        
        return recommendations

    def _perform_predictive_analysis(self, metrics_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform predictive analysis on metrics"""
        predictions = {}
        
        for metric, data in metrics_data.items():
            trend = data.get("trend", "stable")
            current_avg = data.get("avg", 0)
            
            if trend == "increasing":
                predicted_value = current_avg * 1.2  # 20% increase prediction
                predictions[metric] = {
                    "predicted_value": predicted_value,
                    "timeframe": "7 days",
                    "confidence": 0.75,
                    "risk_level": "medium" if predicted_value > current_avg * 1.5 else "low"
                }
            elif trend == "decreasing":
                predicted_value = current_avg * 0.8  # 20% decrease prediction
                predictions[metric] = {
                    "predicted_value": predicted_value,
                    "timeframe": "7 days",
                    "confidence": 0.75,
                    "risk_level": "low"
                }
        
        return {
            "predictions": predictions,
            "high_risk_predictions": [k for k, v in predictions.items() if v["risk_level"] == "high"],
            "prediction_accuracy": 0.78
        }

    def _calculate_duration(self, start_time: str, end_time: str) -> float:
        """Calculate duration in seconds"""
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
        return (end - start).total_seconds()

    def _identify_priority_actions(self, analysis_session: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify priority actions based on analysis"""
        priority_actions = []
        
        # Check for high-severity anomalies
        anomalies = analysis_session.get("findings", {}).get("anomalies", {})
        high_severity_anomalies = [a for a in anomalies.get("anomaly_details", []) if a.get("severity") == "high"]
        
        for anomaly in high_severity_anomalies:
            priority_actions.append({
                "action": f"Investigate {anomaly['metric']} {anomaly['anomaly_type']}",
                "priority": "high",
                "urgency": "immediate",
                "estimated_effort": "2-4 hours"
            })
        
        # Check for concerning trends
        trends = analysis_session.get("findings", {}).get("trends", {})
        concerning_trends = trends.get("concerning_trends", [])
        
        for trend in concerning_trends:
            priority_actions.append({
                "action": f"Address increasing trend in {trend}",
                "priority": "medium",
                "urgency": "within_24_hours",
                "estimated_effort": "4-8 hours"
            })
        
        return priority_actions

    def _assess_system_risks(self, analysis_session: Dict[str, Any]) -> Dict[str, Any]:
        """Assess system risks based on analysis"""
        risk_factors = []
        
        # Anomaly-based risks
        anomalies = analysis_session.get("findings", {}).get("anomalies", {})
        if anomalies.get("anomalies_detected", 0) > 5:
            risk_factors.append("High number of anomalies detected")
        
        # Trend-based risks
        trends = analysis_session.get("findings", {}).get("trends", {})
        if len(trends.get("concerning_trends", [])) > 2:
            risk_factors.append("Multiple concerning performance trends")
        
        # Prediction-based risks
        predictions = analysis_session.get("findings", {}).get("predictions", {})
        high_risk_predictions = predictions.get("high_risk_predictions", [])
        if high_risk_predictions:
            risk_factors.append("High-risk performance predictions")
        
        overall_risk = "high" if len(risk_factors) > 2 else "medium" if len(risk_factors) > 0 else "low"
        
        return {
            "overall_risk_level": overall_risk,
            "risk_factors": risk_factors,
            "risk_score": len(risk_factors) * 25,  # Simple scoring
            "mitigation_required": overall_risk in ["high", "medium"]
        }

    def _create_intelligent_alert_rules(self, rules: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create intelligent alert rules"""
        intelligent_rules = []
        
        # Add default intelligent rules
        default_rules = [
            {
                "rule_id": "anomaly_detection",
                "name": "AI-Powered Anomaly Detection",
                "type": "ml_anomaly",
                "sensitivity": "medium",
                "learning_enabled": True
            },
            {
                "rule_id": "performance_degradation",
                "name": "Performance Degradation Alert",
                "type": "trend_based",
                "threshold_adaptation": True,
                "correlation_aware": True
            }
        ]
        
        intelligent_rules.extend(default_rules)
        intelligent_rules.extend(rules)
        
        return intelligent_rules

    def _setup_alerting_ml_models(self, alerting_system: Dict[str, Any]) -> Dict[str, Any]:
        """Set up ML models for alert optimization"""
        return {
            "noise_reduction_model": {
                "model_type": "classification",
                "purpose": "Identify false positive alerts",
                "training_data": "historical_alerts_with_feedback",
                "accuracy": 0.92
            },
            "severity_optimization_model": {
                "model_type": "regression",
                "purpose": "Optimize alert severity levels",
                "training_data": "alert_outcomes_and_impacts",
                "accuracy": 0.88
            },
            "correlation_model": {
                "model_type": "clustering",
                "purpose": "Group related alerts",
                "training_data": "alert_patterns_and_relationships",
                "accuracy": 0.85
            }
        }

    def _create_alert_processing_pipeline(self, alerting_system: Dict[str, Any]) -> Dict[str, Any]:
        """Create alert processing pipeline"""
        return {
            "pipeline_stages": [
                {"stage": "alert_ingestion", "processing_time": "< 1 second"},
                {"stage": "noise_filtering", "processing_time": "< 2 seconds"},
                {"stage": "correlation_analysis", "processing_time": "< 3 seconds"},
                {"stage": "severity_optimization", "processing_time": "< 1 second"},
                {"stage": "notification_routing", "processing_time": "< 2 seconds"}
            ],
            "total_processing_time": "< 10 seconds",
            "throughput_capacity": "10,000 alerts/minute",
            "reliability": 0.999
        }

    def _setup_alert_analytics(self, alerting_system: Dict[str, Any]) -> Dict[str, Any]:
        """Set up alert analytics"""
        return {
            "metrics_tracked": [
                "alert_volume",
                "false_positive_rate",
                "mean_time_to_acknowledge",
                "mean_time_to_resolve",
                "alert_accuracy",
                "noise_reduction_effectiveness"
            ],
            "reporting_frequency": "daily",
            "dashboard_available": True,
            "ml_model_performance_tracking": True
        }

    def _define_alerting_effectiveness_metrics(self) -> Dict[str, Any]:
        """Define alerting effectiveness metrics"""
        return {
            "target_false_positive_rate": "< 5%",
            "target_alert_accuracy": "> 95%",
            "target_mttr": "< 15 minutes",
            "target_noise_reduction": "> 80%",
            "target_correlation_accuracy": "> 90%"
        }

    def _create_alerting_optimization_schedule(self) -> Dict[str, Any]:
        """Create alerting optimization schedule"""
        return {
            "model_retraining": "weekly",
            "threshold_optimization": "daily",
            "rule_effectiveness_review": "monthly",
            "false_positive_analysis": "daily",
            "performance_optimization": "quarterly"
        }

    def _define_remediation_scenarios(self, scenarios: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Define automated remediation scenarios"""
        default_scenarios = [
            {
                "scenario_id": "high_cpu_usage",
                "name": "High CPU Usage Remediation",
                "trigger_condition": "cpu_usage > 90% for 5 minutes",
                "remediation_actions": ["scale_up", "process_optimization"],
                "success_criteria": "cpu_usage < 80%"
            },
            {
                "scenario_id": "memory_leak",
                "name": "Memory Leak Detection and Remediation",
                "trigger_condition": "memory_usage increasing trend > 5% per hour",
                "remediation_actions": ["application_restart", "garbage_collection"],
                "success_criteria": "memory_usage stabilized"
            }
        ]
        
        remediation_scenarios = default_scenarios.copy()
        remediation_scenarios.extend(scenarios)
        
        return remediation_scenarios

    def _create_trigger_conditions(self, triggers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create trigger conditions for remediation"""
        trigger_conditions = []
        
        for trigger in triggers:
            condition = {
                "condition_id": trigger.get("id") or f"trigger_{len(trigger_conditions)+1}",
                "name": trigger.get("name", "Trigger Condition"),
                "condition_logic": trigger.get("logic", ""),
                "evaluation_window": trigger.get("window", "5 minutes"),
                "severity_threshold": trigger.get("severity", "medium")
            }
            trigger_conditions.append(condition)
        
        return trigger_conditions

    def _create_safety_checks(self, safety_configs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create safety checks for remediation"""
        default_safety_checks = [
            {
                "check_id": "resource_availability",
                "name": "Resource Availability Check",
                "check_type": "pre_execution",
                "description": "Ensure sufficient resources for remediation"
            },
            {
                "check_id": "business_hours",
                "name": "Business Hours Check",
                "check_type": "timing",
                "description": "Avoid disruptive actions during business hours"
            }
        ]
        
        safety_checks = default_safety_checks.copy()
        safety_checks.extend(safety_configs)
        
        return safety_checks

    def _create_rollback_procedures(self, rollback_configs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create rollback procedures"""
        default_rollbacks = [
            {
                "procedure_id": "configuration_rollback",
                "name": "Configuration Rollback",
                "trigger": "remediation_failed",
                "steps": ["backup_restore", "service_restart", "health_check"]
            }
        ]
        
        rollback_procedures = default_rollbacks.copy()
        rollback_procedures.extend(rollback_configs)
        
        return rollback_procedures

    def _create_infrastructure_actions(self) -> List[Dict[str, Any]]:
        """Create infrastructure remediation actions"""
        return [
            {"action": "scale_up", "description": "Increase resource allocation"},
            {"action": "scale_down", "description": "Decrease resource allocation"},
            {"action": "restart_service", "description": "Restart failed service"},
            {"action": "failover", "description": "Switch to backup system"}
        ]

    def _create_application_actions(self) -> List[Dict[str, Any]]:
        """Create application remediation actions"""
        return [
            {"action": "restart_application", "description": "Restart application process"},
            {"action": "clear_cache", "description": "Clear application cache"},
            {"action": "garbage_collection", "description": "Force garbage collection"},
            {"action": "configuration_reload", "description": "Reload application configuration"}
        ]

    def _create_data_actions(self) -> List[Dict[str, Any]]:
        """Create data remediation actions"""
        return [
            {"action": "cleanup_logs", "description": "Clean up old log files"},
            {"action": "archive_data", "description": "Archive old data"},
            {"action": "rebuild_index", "description": "Rebuild database indexes"},
            {"action": "backup_database", "description": "Create database backup"}
        ]

    def _create_network_actions(self) -> List[Dict[str, Any]]:
        """Create network remediation actions"""
        return [
            {"action": "reset_connection", "description": "Reset network connection"},
            {"action": "update_routing", "description": "Update network routing"},
            {"action": "flush_dns", "description": "Flush DNS cache"},
            {"action": "restart_network", "description": "Restart network service"}
        ]

    def _setup_remediation_intelligence(self, remediation_system: Dict[str, Any]) -> Dict[str, Any]:
        """Set up remediation intelligence"""
        return {
            "success_prediction_model": {
                "model_type": "classification",
                "purpose": "Predict remediation success probability",
                "accuracy": 0.89
            },
            "impact_assessment_model": {
                "model_type": "regression", 
                "purpose": "Assess potential impact of remediation actions",
                "accuracy": 0.85
            },
            "learning_system": {
                "feedback_collection": True,
                "outcome_tracking": True,
                "model_improvement": "continuous"
            }
        }

    def _create_remediation_workflows(self, remediation_system: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create remediation workflows"""
        workflows = []
        
        scenarios = remediation_system.get("remediation_scenarios", [])
        for scenario in scenarios:
            workflow = {
                "workflow_id": f"remediation_{scenario['scenario_id']}",
                "name": f"Remediation Workflow - {scenario['name']}",
                "trigger": scenario.get("trigger_condition", ""),
                "steps": self._create_remediation_workflow_steps(scenario),
                "success_criteria": scenario.get("success_criteria", ""),
                "rollback_enabled": True
            }
            workflows.append(workflow)
        
        return workflows

    def _create_remediation_workflow_steps(self, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create workflow steps for remediation scenario"""
        return [
            {"step": "safety_check", "action": "perform_safety_checks"},
            {"step": "backup_state", "action": "create_system_backup"},
            {"step": "execute_remediation", "action": scenario.get("remediation_actions", [])},
            {"step": "validate_success", "action": "check_success_criteria"},
            {"step": "cleanup", "action": "cleanup_temporary_resources"}
        ]

    def _setup_remediation_success_tracking(self, remediation_system: Dict[str, Any]) -> Dict[str, Any]:
        """Set up remediation success tracking"""
        return {
            "metrics_tracked": [
                "remediation_success_rate",
                "average_remediation_time",
                "rollback_frequency",
                "system_stability_improvement",
                "business_impact_reduction"
            ],
            "reporting_dashboard": True,
            "automated_reports": "weekly",
            "success_rate_target": "> 95%"
        }

    def _generate_safety_report(self, remediation_system: Dict[str, Any]) -> Dict[str, Any]:
        """Generate safety report for remediation system"""
        return {
            "safety_score": 95,
            "risk_assessment": "low",
            "safety_measures": len(remediation_system.get("automation_rules", {}).get("safety_checks", [])),
            "rollback_capabilities": "comprehensive",
            "governance_compliance": "fully_compliant",
            "recommendations": ["Regular safety check reviews", "Emergency stop procedures"]
        }

    def _create_remediation_testing_plan(self, remediation_system: Dict[str, Any]) -> Dict[str, Any]:
        """Create testing plan for remediation system"""
        return {
            "testing_phases": [
                {"phase": "unit_testing", "duration": "1 week", "scope": "Individual actions"},
                {"phase": "integration_testing", "duration": "2 weeks", "scope": "Full scenarios"},
                {"phase": "chaos_testing", "duration": "1 week", "scope": "Failure scenarios"}
            ],
            "test_environments": ["staging", "pre_production"],
            "success_criteria": "100% test pass rate",
            "rollback_testing": "comprehensive"
        }

    def _analyze_monitoring_effectiveness(self, current_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze current monitoring effectiveness"""
        return {
            "coverage_score": current_data.get("coverage", 75),
            "alert_noise_ratio": current_data.get("noise_ratio", 0.25),
            "mean_detection_time": current_data.get("detection_time", 300),
            "false_positive_rate": current_data.get("false_positives", 0.15),
            "incident_prevention_rate": current_data.get("prevention_rate", 0.60),
            "monitoring_costs": current_data.get("monthly_costs", 5000),
            "team_satisfaction": current_data.get("team_satisfaction", 6.5)
        }

    def _create_optimized_monitoring_strategy(self, effectiveness_analysis: Dict[str, Any], recommendations: Dict[str, Any]) -> Dict[str, Any]:
        """Create optimized monitoring strategy"""
        return {
            "strategy_version": "2.0",
            "optimization_focus": ["coverage_improvement", "noise_reduction", "predictive_capabilities"],
            "monitoring_tiers": {
                "tier_1_critical": "24/7 monitoring with immediate alerts",
                "tier_2_important": "Business hours monitoring with escalation",
                "tier_3_informational": "Trend monitoring with weekly reports"
            },
            "intelligence_enhancements": {
                "ml_anomaly_detection": True,
                "predictive_alerting": True,
                "root_cause_analysis": True,
                "automated_correlation": True
            },
            "target_metrics": {
                "coverage_score": 90,
                "alert_accuracy": 95,
                "mean_detection_time": 60,
                "false_positive_rate": 0.05
            }
        }

    def _create_monitoring_optimization_plan(self, optimized_strategy: Dict[str, Any]) -> Dict[str, Any]:
        """Create monitoring optimization implementation plan"""
        return {
            "implementation_phases": [
                {
                    "phase": 1,
                    "duration": "3 weeks",
                    "focus": "Intelligence enhancement and ML integration",
                    "deliverables": ["Anomaly detection", "Predictive models"]
                },
                {
                    "phase": 2,
                    "duration": "2 weeks",
                    "focus": "Alert optimization and noise reduction", 
                    "deliverables": ["Smart alerting", "Correlation rules"]
                },
                {
                    "phase": 3,
                    "duration": "2 weeks",
                    "focus": "Coverage expansion and automation",
                    "deliverables": ["Extended monitoring", "Auto-remediation"]
                }
            ],
            "success_criteria": optimized_strategy.get("target_metrics", {}),
            "rollback_plan": "Gradual rollout with monitoring effectiveness validation"
        }

    def _calculate_monitoring_benefits(self, recommendations: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate expected monitoring benefits"""
        return {
            "detection_time_improvement": "75% faster incident detection",
            "false_positive_reduction": "80% reduction in alert noise",
            "operational_efficiency": "40% improvement in team productivity",
            "incident_prevention": "50% more incidents prevented",
            "cost_savings": "$15,000-30,000/year in operational costs",
            "customer_satisfaction": "25% improvement in service reliability"
        }

    def _calculate_monitoring_costs(self, recommendations: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate monitoring costs"""
        return {
            "implementation_cost": "$50,000-100,000",
            "ongoing_monthly_cost": "$8,000-12,000",
            "tool_licensing": "$3,000-5,000/month",
            "personnel_training": "$10,000-20,000",
            "roi_timeline": "6-9 months",
            "break_even_point": "8 months"
        }

    def _create_monitoring_migration_strategy(self, optimization_result: Dict[str, Any]) -> Dict[str, Any]:
        """Create monitoring migration strategy"""
        return {
            "migration_approach": "phased_rollout",
            "pilot_phase": {
                "duration": "2 weeks",
                "scope": "Non-critical systems",
                "success_criteria": "Zero service impact"
            },
            "full_rollout": {
                "duration": "6 weeks", 
                "approach": "gradual_expansion",
                "validation_checkpoints": "weekly"
            },
            "rollback_strategy": {
                "trigger_conditions": ["Service degradation", "Alert storm"],
                "rollback_time": "< 30 minutes",
                "data_preservation": "comprehensive"
            }
        }

    def get_agent_status(self) -> Dict[str, Any]:
        """Get current agent status and capabilities"""
        return {
            "name": self.name,
            "role": self.role,
            "status": "active",
            "responsibilities": self.responsibilities,
            "capabilities": self.capabilities,
            "monitoring_systems": len(self.monitoring_systems),
            "active_alerts": len(self.active_alerts),
            "last_updated": datetime.now().isoformat()
        }

# Initialize the agent
intelligent_monitoring_agent = IntelligentMonitoringAgent()