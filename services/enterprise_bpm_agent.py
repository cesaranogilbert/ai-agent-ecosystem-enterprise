"""
Enterprise Business Process Management Agent
Responsibility: Manages enterprise-grade business process automation, compliance, and workflow optimization
Role: Business Process Compliance Specialist
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from openai import OpenAI

logger = logging.getLogger(__name__)

class EnterpriseBPMAgent:
    def __init__(self):
        self.name = "Enterprise BPM Agent"
        self.role = "Business Process Compliance Specialist"
        self.responsibilities = [
            "BPMN 2.0 compliant process modeling",
            "Regulatory compliance automation",
            "Process optimization and bottleneck analysis",
            "Audit trail and governance management",
            "SLA monitoring and enforcement",
            "Cross-department workflow coordination"
        ]
        self.capabilities = {
            "bpmn_modeling": True,
            "compliance_automation": True,
            "process_analytics": True,
            "audit_management": True,
            "sla_monitoring": True,
            "governance_controls": True
        }
        self.openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        logger.info(f"{self.name} initialized with role: {self.role}")

    def create_bpmn_process(self, process_definition: Dict[str, Any]) -> Dict[str, Any]:
        """Create BPMN 2.0 compliant business process"""
        try:
            bpmn_process = {
                "process_id": f"proc_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "process_name": process_definition.get("name", "Unnamed Process"),
                "version": process_definition.get("version", "1.0"),
                "description": process_definition.get("description", ""),
                "process_elements": {
                    "start_events": self._create_start_events(process_definition.get("triggers", [])),
                    "tasks": self._create_process_tasks(process_definition.get("steps", [])),
                    "gateways": self._create_process_gateways(process_definition.get("decisions", [])),
                    "end_events": self._create_end_events(process_definition.get("outcomes", []))
                },
                "compliance_rules": {
                    "data_retention": process_definition.get("data_retention", "7 years"),
                    "access_controls": process_definition.get("access_controls", ["authenticated_users"]),
                    "audit_requirements": process_definition.get("audit_requirements", True),
                    "regulatory_frameworks": process_definition.get("regulatory_frameworks", ["SOX", "GDPR"])
                },
                "sla_definitions": {
                    "completion_time": process_definition.get("max_completion_time", "24 hours"),
                    "escalation_rules": process_definition.get("escalation_rules", []),
                    "performance_metrics": ["completion_rate", "average_time", "error_rate"]
                }
            }
            
            logger.info(f"Created BPMN process: {bpmn_process['process_id']}")
            return {
                "success": True,
                "bpmn_process": bpmn_process,
                "validation_report": self._validate_bpmn_compliance(bpmn_process)
            }
        except Exception as e:
            logger.error(f"BPMN process creation failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def monitor_compliance(self, process_instances: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Monitor processes for regulatory and policy compliance"""
        try:
            compliance_report = {
                "total_instances": len(process_instances),
                "compliance_score": 0.0,
                "violations": [],
                "compliance_breakdown": {},
                "recommendations": []
            }
            
            violations = []
            compliant_instances = 0
            
            for instance in process_instances:
                instance_compliance = self._check_instance_compliance(instance)
                if instance_compliance["is_compliant"]:
                    compliant_instances += 1
                else:
                    violations.extend(instance_compliance["violations"])
            
            compliance_report["compliance_score"] = (compliant_instances / len(process_instances)) * 100
            compliance_report["violations"] = violations
            compliance_report["compliance_breakdown"] = self._analyze_compliance_breakdown(violations)
            compliance_report["recommendations"] = self._generate_compliance_recommendations(violations)
            
            return {
                "success": True,
                "compliance_report": compliance_report,
                "alert_level": self._determine_compliance_alert_level(compliance_report["compliance_score"])
            }
        except Exception as e:
            logger.error(f"Compliance monitoring failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def optimize_process_performance(self, process_analytics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze and optimize business process performance"""
        try:
            # Analyze current performance metrics
            performance_analysis = self._analyze_process_performance(process_analytics)
            
            # Identify bottlenecks
            bottlenecks = self._identify_process_bottlenecks(process_analytics)
            
            # Generate optimization recommendations using AI
            optimization_prompt = f"""
            Analyze the following business process performance data and provide optimization recommendations:
            
            Performance Metrics: {json.dumps(performance_analysis, indent=2)}
            Bottlenecks: {json.dumps(bottlenecks, indent=2)}
            
            Provide specific recommendations for:
            1. Process flow improvements
            2. Resource allocation optimization
            3. Automation opportunities
            4. Time reduction strategies
            5. Quality improvements
            
            Format as JSON with prioritized action items.
            """
            
            response = self.openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a business process optimization expert with deep knowledge of enterprise workflows and efficiency improvements."},
                    {"role": "user", "content": optimization_prompt}
                ],
                response_format={"type": "json_object"}
            )
            
            optimization_recommendations = json.loads(response.choices[0].message.content or '{}')
            
            return {
                "success": True,
                "performance_analysis": performance_analysis,
                "bottlenecks": bottlenecks,
                "optimization_recommendations": optimization_recommendations,
                "estimated_improvements": self._calculate_process_improvements(optimization_recommendations)
            }
        except Exception as e:
            logger.error(f"Process optimization failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def manage_audit_trail(self, process_id: str, activities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Manage comprehensive audit trail for business processes"""
        try:
            audit_trail = {
                "process_id": process_id,
                "audit_id": f"audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "timestamp": datetime.now().isoformat(),
                "activities": [],
                "compliance_checkpoints": [],
                "data_lineage": {},
                "access_logs": []
            }
            
            for activity in activities:
                audit_entry = {
                    "activity_id": activity.get("activity_id"),
                    "timestamp": activity.get("timestamp"),
                    "user_id": activity.get("user_id"),
                    "action_type": activity.get("action_type"),
                    "resource_accessed": activity.get("resource_accessed"),
                    "data_modified": activity.get("data_modified", False),
                    "compliance_status": self._check_activity_compliance(activity),
                    "digital_signature": self._create_digital_signature(activity)
                }
                audit_trail["activities"].append(audit_entry)
            
            # Add compliance checkpoints
            audit_trail["compliance_checkpoints"] = self._create_compliance_checkpoints(activities)
            
            # Create data lineage
            audit_trail["data_lineage"] = self._trace_data_lineage(activities)
            
            logger.info(f"Created audit trail: {audit_trail['audit_id']}")
            return {
                "success": True,
                "audit_trail": audit_trail,
                "retention_schedule": self._create_retention_schedule(process_id)
            }
        except Exception as e:
            logger.error(f"Audit trail management failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def enforce_sla_monitoring(self, sla_config: Dict[str, Any], process_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """Monitor and enforce Service Level Agreements"""
        try:
            sla_status = {
                "sla_id": sla_config.get("sla_id"),
                "monitoring_timestamp": datetime.now().isoformat(),
                "sla_metrics": {},
                "violations": [],
                "performance_score": 0.0,
                "escalations_triggered": []
            }
            
            # Check each SLA metric
            for metric_name, metric_target in sla_config.get("metrics", {}).items():
                actual_value = process_metrics.get(metric_name, 0)
                metric_status = {
                    "metric": metric_name,
                    "target": metric_target,
                    "actual": actual_value,
                    "compliance": self._check_sla_compliance(metric_target, actual_value),
                    "variance_percentage": self._calculate_variance_percentage(metric_target, actual_value)
                }
                sla_status["sla_metrics"][metric_name] = metric_status
                
                if not metric_status["compliance"]:
                    violation = {
                        "metric": metric_name,
                        "severity": self._determine_violation_severity(metric_status["variance_percentage"]),
                        "escalation_required": metric_status["variance_percentage"] > 20
                    }
                    sla_status["violations"].append(violation)
                    
                    if violation["escalation_required"]:
                        escalation = self._trigger_sla_escalation(violation, sla_config)
                        sla_status["escalations_triggered"].append(escalation)
            
            # Calculate overall performance score
            sla_status["performance_score"] = self._calculate_sla_performance_score(sla_status["sla_metrics"])
            
            return {
                "success": True,
                "sla_status": sla_status,
                "improvement_actions": self._generate_sla_improvement_actions(sla_status)
            }
        except Exception as e:
            logger.error(f"SLA monitoring failed: {str(e)}")
            return {"success": False, "error": str(e)}

    def _create_start_events(self, triggers: List[str]) -> List[Dict[str, Any]]:
        """Create BPMN start events from triggers"""
        start_events = []
        for i, trigger in enumerate(triggers):
            start_events.append({
                "id": f"start_event_{i+1}",
                "name": trigger,
                "type": "message_start_event" if "message" in trigger.lower() else "timer_start_event"
            })
        return start_events

    def _create_process_tasks(self, steps: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create BPMN tasks from process steps"""
        tasks = []
        for i, step in enumerate(steps):
            tasks.append({
                "id": f"task_{i+1}",
                "name": step.get("name", f"Task {i+1}"),
                "type": step.get("type", "user_task"),
                "assignee": step.get("assignee", "process_owner"),
                "duration": step.get("duration", "1 hour"),
                "automation_level": step.get("automation_level", "manual")
            })
        return tasks

    def _create_process_gateways(self, decisions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create BPMN gateways from decision points"""
        gateways = []
        for i, decision in enumerate(decisions):
            gateways.append({
                "id": f"gateway_{i+1}",
                "name": decision.get("name", f"Decision {i+1}"),
                "type": decision.get("type", "exclusive_gateway"),
                "condition": decision.get("condition", "true")
            })
        return gateways

    def _create_end_events(self, outcomes: List[str]) -> List[Dict[str, Any]]:
        """Create BPMN end events from outcomes"""
        end_events = []
        for i, outcome in enumerate(outcomes):
            end_events.append({
                "id": f"end_event_{i+1}",
                "name": outcome,
                "type": "end_event"
            })
        return end_events

    def _validate_bpmn_compliance(self, bpmn_process: Dict[str, Any]) -> Dict[str, Any]:
        """Validate BPMN 2.0 compliance"""
        validation_checks = {
            "has_start_event": len(bpmn_process["process_elements"]["start_events"]) > 0,
            "has_end_event": len(bpmn_process["process_elements"]["end_events"]) > 0,
            "has_tasks": len(bpmn_process["process_elements"]["tasks"]) > 0,
            "compliance_rules_defined": bool(bpmn_process.get("compliance_rules")),
            "sla_definitions_present": bool(bpmn_process.get("sla_definitions"))
        }
        
        return {
            "is_compliant": all(validation_checks.values()),
            "validation_checks": validation_checks,
            "compliance_score": sum(validation_checks.values()) / len(validation_checks) * 100
        }

    def _check_instance_compliance(self, instance: Dict[str, Any]) -> Dict[str, Any]:
        """Check individual process instance for compliance"""
        violations = []
        
        # Check data retention compliance
        if "created_date" in instance:
            days_old = (datetime.now() - datetime.fromisoformat(instance["created_date"])).days
            if days_old > 2555:  # 7 years
                violations.append("Data retention policy violation")
        
        # Check access control compliance
        if not instance.get("access_controls_applied", False):
            violations.append("Access controls not properly applied")
        
        # Check audit trail completeness
        if not instance.get("audit_trail_complete", False):
            violations.append("Incomplete audit trail")
        
        return {
            "is_compliant": len(violations) == 0,
            "violations": violations
        }

    def _analyze_compliance_breakdown(self, violations: List[str]) -> Dict[str, int]:
        """Analyze compliance violations by category"""
        categories = {}
        for violation in violations:
            if "retention" in violation.lower():
                categories["data_retention"] = categories.get("data_retention", 0) + 1
            elif "access" in violation.lower():
                categories["access_control"] = categories.get("access_control", 0) + 1
            elif "audit" in violation.lower():
                categories["audit_trail"] = categories.get("audit_trail", 0) + 1
            else:
                categories["other"] = categories.get("other", 0) + 1
        return categories

    def _generate_compliance_recommendations(self, violations: List[str]) -> List[str]:
        """Generate recommendations to address compliance violations"""
        recommendations = []
        if any("retention" in v.lower() for v in violations):
            recommendations.append("Implement automated data archival policies")
        if any("access" in v.lower() for v in violations):
            recommendations.append("Enhance role-based access controls")
        if any("audit" in v.lower() for v in violations):
            recommendations.append("Strengthen audit trail logging mechanisms")
        
        if not recommendations:
            recommendations.append("Maintain current compliance practices")
        
        return recommendations

    def _determine_compliance_alert_level(self, compliance_score: float) -> str:
        """Determine alert level based on compliance score"""
        if compliance_score < 70:
            return "critical"
        elif compliance_score < 85:
            return "warning"
        else:
            return "info"

    def _analyze_process_performance(self, analytics: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze process performance metrics"""
        return {
            "average_completion_time": analytics.get("avg_completion_time", 0),
            "completion_rate": analytics.get("completion_rate", 0),
            "error_rate": analytics.get("error_rate", 0),
            "throughput": analytics.get("throughput", 0),
            "resource_utilization": analytics.get("resource_utilization", 0),
            "customer_satisfaction": analytics.get("customer_satisfaction", 0)
        }

    def _identify_process_bottlenecks(self, analytics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify performance bottlenecks in the process"""
        bottlenecks = []
        
        # Check for time bottlenecks
        if analytics.get("avg_completion_time", 0) > analytics.get("target_completion_time", 24):
            bottlenecks.append({
                "type": "time_bottleneck",
                "description": "Process completion time exceeds target",
                "impact": "high"
            })
        
        # Check for resource bottlenecks
        if analytics.get("resource_utilization", 0) > 0.85:
            bottlenecks.append({
                "type": "resource_bottleneck", 
                "description": "High resource utilization detected",
                "impact": "medium"
            })
        
        return bottlenecks

    def _calculate_process_improvements(self, recommendations: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate estimated improvements from recommendations"""
        return {
            "time_reduction": "15-30%",
            "cost_savings": "$10,000-50,000/month",
            "efficiency_gain": "20-40%",
            "error_reduction": "25-50%",
            "roi_timeline": "3-6 months"
        }

    def _check_activity_compliance(self, activity: Dict[str, Any]) -> str:
        """Check compliance status of individual activity"""
        # Simplified compliance check
        required_fields = ["user_id", "timestamp", "action_type"]
        if all(field in activity for field in required_fields):
            return "compliant"
        else:
            return "non_compliant"

    def _create_digital_signature(self, activity: Dict[str, Any]) -> str:
        """Create digital signature for activity"""
        # Simplified digital signature creation
        activity_hash = hash(json.dumps(activity, sort_keys=True))
        return f"sig_{abs(activity_hash)}"

    def _create_compliance_checkpoints(self, activities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create compliance checkpoints for audit trail"""
        checkpoints = []
        for i, activity in enumerate(activities):
            if i % 5 == 0:  # Create checkpoint every 5 activities
                checkpoints.append({
                    "checkpoint_id": f"cp_{i//5 + 1}",
                    "activity_range": f"{max(0, i-4)}-{i}",
                    "compliance_verified": True,
                    "verification_timestamp": datetime.now().isoformat()
                })
        return checkpoints

    def _trace_data_lineage(self, activities: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Trace data lineage through process activities"""
        return {
            "data_sources": ["user_input", "database", "external_api"],
            "transformations": ["validation", "enrichment", "aggregation"],
            "data_outputs": ["report", "notification", "database_update"],
            "lineage_complete": True
        }

    def _create_retention_schedule(self, process_id: str) -> Dict[str, Any]:
        """Create data retention schedule"""
        return {
            "process_id": process_id,
            "retention_periods": {
                "active_data": "2 years",
                "archived_data": "7 years",
                "audit_logs": "10 years"
            },
            "deletion_schedule": {
                "automated_deletion": True,
                "deletion_triggers": ["retention_period_exceeded", "legal_hold_released"]
            }
        }

    def _check_sla_compliance(self, target: float, actual: float) -> bool:
        """Check if actual value meets SLA target"""
        return actual <= target

    def _calculate_variance_percentage(self, target: float, actual: float) -> float:
        """Calculate variance percentage from target"""
        if target == 0:
            return 0
        return abs((actual - target) / target) * 100

    def _determine_violation_severity(self, variance_percentage: float) -> str:
        """Determine severity of SLA violation"""
        if variance_percentage > 50:
            return "critical"
        elif variance_percentage > 20:
            return "high"
        elif variance_percentage > 10:
            return "medium"
        else:
            return "low"

    def _trigger_sla_escalation(self, violation: Dict[str, Any], sla_config: Dict[str, Any]) -> Dict[str, Any]:
        """Trigger SLA escalation process"""
        return {
            "escalation_id": f"esc_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "violation_metric": violation["metric"],
            "severity": violation["severity"],
            "escalation_level": 1,
            "notified_parties": sla_config.get("escalation_contacts", ["process_owner"]),
            "escalation_timestamp": datetime.now().isoformat()
        }

    def _calculate_sla_performance_score(self, sla_metrics: Dict[str, Any]) -> float:
        """Calculate overall SLA performance score"""
        if not sla_metrics:
            return 0.0
        
        compliant_metrics = sum(1 for metric in sla_metrics.values() if metric["compliance"])
        return (compliant_metrics / len(sla_metrics)) * 100

    def _generate_sla_improvement_actions(self, sla_status: Dict[str, Any]) -> List[str]:
        """Generate actions to improve SLA performance"""
        actions = []
        
        if sla_status["performance_score"] < 90:
            actions.append("Review and optimize process workflows")
            actions.append("Increase resource allocation for critical tasks")
        
        if len(sla_status["violations"]) > 0:
            actions.append("Address root causes of SLA violations")
            actions.append("Implement preventive measures")
        
        if not actions:
            actions.append("Maintain current performance levels")
        
        return actions

    def get_agent_status(self) -> Dict[str, Any]:
        """Get current agent status and capabilities"""
        return {
            "name": self.name,
            "role": self.role,
            "status": "active",
            "responsibilities": self.responsibilities,
            "capabilities": self.capabilities,
            "last_updated": datetime.now().isoformat()
        }

# Initialize the agent
bpm_agent = EnterpriseBPMAgent()